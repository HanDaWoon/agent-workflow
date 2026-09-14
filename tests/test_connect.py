"""Exercise the public connection command using disposable Git projects."""

from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/connect.py"
SOURCE = ROOT / "skills/engineering-workflow"


class ConnectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="workflow-connect-")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project with spaces"
        self.project.mkdir()
        subprocess.run(["git", "init", "-q", str(self.project)], check=True)

    def run_connect(self, agent, apply=True):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--project", str(self.project),
             "--agent", agent] + (["--apply"] if apply else []),
            capture_output=True, text=True,
        )

    def test_preview_writes_nothing(self):
        result = self.run_connect("both", apply=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.project.iterdir()}, {".git"})
        self.assertIn("CLAUDE.md", result.stdout)
        self.assertIn("AGENTS.md", result.stdout)

    def test_each_selection_and_repetition(self):
        for agent, folders, instructions in [
            ("codex", [".agents"], ["AGENTS.md"]),
            ("claude", [".claude"], ["CLAUDE.md"]),
            ("both", [".agents", ".claude"], ["AGENTS.md", "CLAUDE.md"]),
        ]:
            with self.subTest(agent=agent), tempfile.TemporaryDirectory() as location:
                original = self.project
                self.project = Path(location)
                subprocess.run(["git", "init", "-q", location], check=True)
                try:
                    result = self.run_connect(agent)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    for folder in folders:
                        link = self.project / folder / "skills/engineering-workflow"
                        self.assertTrue(link.is_symlink())
                        self.assertEqual(link.resolve(), SOURCE.resolve())
                        self.assertEqual((link / "references/execution.md").read_bytes(),
                                         (SOURCE / "references/execution.md").read_bytes())
                    self.assertEqual({p.name for p in self.project.iterdir()},
                                     {".git", *folders, *instructions})
                    before = {n: (self.project / n).read_bytes() for n in instructions}
                    self.assertEqual(self.run_connect(agent).returncode, 0)
                    self.assertEqual(before, {n: (self.project / n).read_bytes() for n in instructions})
                    if agent == "both":
                        self.assertIn("@AGENTS.md", (self.project / "CLAUDE.md").read_text())
                        self.assertEqual(self.run_connect("claude").returncode, 0)
                        self.assertTrue((self.project / ".agents").is_dir())
                finally:
                    self.project = original

    def test_claude_preserves_and_imports_existing_project_rules(self):
        original = b"# User standards\r\nPreserve me.\r\n"
        (self.project / "AGENTS.md").write_bytes(original)
        (self.project / "CLAUDE.md").write_bytes(b"# Claude rules\n")
        self.assertEqual(self.run_connect("claude").returncode, 0)
        self.assertEqual((self.project / "AGENTS.md").read_bytes(), original)
        self.assertTrue((self.project / "CLAUDE.md").read_bytes().startswith(b"# Claude rules\n"))
        self.assertIn("@AGENTS.md", (self.project / "CLAUDE.md").read_text())

    def test_conflicting_second_target_prevents_all_writes(self):
        conflict = self.project / ".claude/skills/engineering-workflow"
        conflict.mkdir(parents=True)
        (conflict / "user.md").write_text("keep")
        result = self.run_connect("both")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.project / ".agents").exists())
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.assertEqual((conflict / "user.md").read_text(), "keep")

    def test_modified_managed_block_is_preserved(self):
        self.assertEqual(self.run_connect("codex").returncode, 0)
        path = self.project / "AGENTS.md"
        edited = path.read_bytes().replace(b"For implementation", b"For user-approved implementation")
        path.write_bytes(edited)
        self.assertNotEqual(self.run_connect("codex").returncode, 0)
        self.assertEqual(path.read_bytes(), edited)

    def test_existing_source_pointer_is_not_duplicated(self):
        path = self.project / "AGENTS.md"
        path.write_text("Use engineering-workflow from the shared source.\n")
        before = path.read_bytes()
        self.assertNotEqual(self.run_connect("codex").returncode, 0)
        self.assertEqual(path.read_bytes(), before)
        self.assertFalse((self.project / ".agents").exists())

    def test_symlink_parent_and_instruction_are_preserved(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside)
            (self.project / ".claude").symlink_to(external, target_is_directory=True)
            self.assertNotEqual(self.run_connect("claude").returncode, 0)
            self.assertEqual(list(external.iterdir()), [])
            (self.project / ".claude").unlink()
            (external / "rules.md").write_text("keep")
            (self.project / "CLAUDE.md").symlink_to(external / "rules.md")
            self.assertNotEqual(self.run_connect("claude").returncode, 0)
            self.assertEqual((external / "rules.md").read_text(), "keep")

    def test_missing_project_is_not_created(self):
        self.project = self.project / "missing"
        self.assertNotEqual(self.run_connect("both").returncode, 0)
        self.assertFalse(self.project.exists())

    def test_hardlinked_instruction_cannot_change_external_file(self):
        external = Path(self.temp.name) / "shared.md"
        external.write_text("Existing shared instructions.\n")
        os.link(external, self.project / "CLAUDE.md")
        result = self.run_connect("both")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(external.read_text(), "Existing shared instructions.\n")
        self.assertFalse((self.project / ".agents").exists())

    def test_override_precedence_requires_manual_merge(self):
        override = self.project / "AGENTS.override.md"
        override.write_text("Existing override.\n")
        self.assertNotEqual(self.run_connect("both").returncode, 0)
        self.assertEqual(override.read_text(), "Existing override.\n")
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.assertFalse((self.project / ".agents").exists())


if __name__ == "__main__":
    unittest.main()
