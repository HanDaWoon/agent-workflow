#!/usr/bin/env python3
"""Connect this workflow source to a selected project's coding agents."""

import argparse
import difflib
import os
from pathlib import Path
import sys
from urllib.parse import quote


SOURCE = Path(__file__).resolve().parents[1] / "skills/engineering-workflow"
BEGIN = "<!-- agent-workflow:begin -->"
END = "<!-- agent-workflow:end -->"
TARGETS = {
    "codex": (".agents/skills/engineering-workflow", "AGENTS.md"),
    "claude": (".claude/skills/engineering-workflow", "CLAUDE.md"),
}


def check_path(project, path):
    """Keep all writes inside the selected checkout, including existing parents."""
    for parent in path.relative_to(project).parents:
        candidate = project / parent
        if candidate.is_symlink():
            raise ValueError(f"심볼릭 링크 경유 경로는 자동 변경하지 않습니다: {candidate}")
        if candidate.exists() and not candidate.is_dir():
            raise ValueError(f"디렉터리가 아닌 경로입니다: {candidate}")


def instruction_block(import_agents):
    skill_path = quote(str(SOURCE / "SKILL.md"), safe="/")
    body = ("@AGENTS.md\n\n" if import_agents else "") + (
        "For implementation, resumption, and work-planning requests, read "
        f"[Engineering Workflow]({skill_path}) directly and follow its applicable route. "
        "Open that exact file before using directory search to conclude it is unavailable. "
        "Read the project's existing instructions and verification requirements. "
        "For questions and reading requests, answer directly from the necessary evidence."
    )
    return f"{BEGIN}\n{body}\n{END}\n"


def plan(project, agents):
    if not (project / ".git").exists():
        raise ValueError("--project에는 기존 Git 프로젝트의 루트 경로를 지정하세요.")
    if not (SOURCE / "SKILL.md").is_file():
        raise ValueError(f"스킬 원본을 찾을 수 없습니다: {SOURCE}")
    if "codex" in agents and os.path.lexists(project / "AGENTS.override.md"):
        raise ValueError("AGENTS.override.md가 AGENTS.md보다 우선합니다. 기존 진입 지침을 직접 병합하세요.")
    actions = []
    for agent in agents:
        relative, filename = TARGETS[agent]
        link = project / relative
        instruction = project / filename
        check_path(project, link)
        check_path(project, instruction)
        if os.path.lexists(link):
            if not link.is_symlink() or link.resolve() != SOURCE.resolve():
                raise ValueError(f"기존 스킬 경로를 보존합니다. 직접 검토 후 다시 실행하세요: {link}")
        else:
            actions.append(("link", link, None, SOURCE))
        if instruction.is_symlink() or (instruction.exists() and not instruction.is_file()):
            raise ValueError(f"기존 지침 경로를 자동 변경하지 않습니다: {instruction}")
        if instruction.exists() and instruction.stat().st_nlink > 1:
            raise ValueError(f"하드링크 지침을 보존합니다. 공유 파일을 직접 검토하세요: {instruction}")
        before = instruction.read_bytes() if instruction.exists() else None
        text = (before or b"").decode("utf-8")
        shared = project / "AGENTS.md"
        if agent == "claude" and shared.is_symlink():
            raise ValueError(f"공유 지침의 심볼릭 링크를 직접 검토하세요: {shared}")
        block = instruction_block(agent == "claude" and
                                  (shared.is_file() or "codex" in agents))
        if BEGIN in text or END in text:
            if text.count(BEGIN) != 1 or text.count(END) != 1 or block not in text:
                raise ValueError(f"기존 연결 블록이 다릅니다. 지침을 보존하고 직접 병합하세요: {instruction}")
            continue
        if "engineering-workflow" in text:
            raise ValueError(f"이미 workflow 지침이 있습니다. 중복을 피하도록 직접 병합하세요: {instruction}")
        separator = ("\n" if text.endswith("\n") else "\n\n") if text else ""
        after = (before or b"") + (separator + block).encode("utf-8")
        actions.append(("instruction", instruction, before, after))
    return actions


def apply(actions):
    # Preflight all paths before the first mutation; concurrent edits remain an error.
    for kind, path, before, after in actions:
        if kind == "link":
            if os.path.lexists(path):
                raise ValueError(f"검토 후 경로가 변경되었습니다: {path}")
        elif (path.read_bytes() if path.exists() else None) != before:
            raise ValueError(f"검토 후 지침이 변경되었습니다: {path}")
    for kind, path, before, after in actions:
        path.parent.mkdir(parents=True, exist_ok=True)
        if kind == "link":
            path.symlink_to(after, target_is_directory=True)
        elif before is None:
            with path.open("xb") as stream:
                stream.write(after)
        else:
            # Preserve existing bytes and file permissions.
            with path.open("r+b") as stream:
                if stream.read() != before:
                    raise ValueError(f"적용 중 지침이 변경되었습니다: {path}")
                stream.write(after[len(before):])
        print(f"적용: {path}")


def main():
    parser = argparse.ArgumentParser(description="agent-workflow 프로젝트 연결 (기본: 미리보기)")
    parser.add_argument("--project", type=Path, required=True, help="대상 Git 프로젝트 루트")
    parser.add_argument("--agent", choices=["codex", "claude", "both"], required=True,
                        help="추가할 연결. 기존의 다른 연결은 제거하지 않습니다.")
    parser.add_argument("--apply", action="store_true", help="표시한 연결을 실제 적용")
    args = parser.parse_args()
    try:
        project = args.project.expanduser().resolve(strict=True)
        agents = list(TARGETS) if args.agent == "both" else [args.agent]
        actions = plan(project, agents)
        for kind, path, before, after in actions:
            if kind == "link":
                print(f"연결 예정: {path} -> {after}")
            else:
                print("".join(difflib.unified_diff(
                    (before or b"").decode().splitlines(keepends=True),
                    after.decode().splitlines(keepends=True),
                    fromfile=str(path), tofile=str(path))), end="")
        if args.apply:
            apply(actions)
            # Verify the full requested state after writing.
            if plan(project, agents):
                raise ValueError("적용 후 연결 검증이 완료되지 않았습니다.")
            print("연결 확인 완료. 새 에이전트 세션에서 진입을 확인하세요.")
        else:
            print("변경하지 않았습니다. 적용하려면 같은 명령에 --apply를 추가하세요.")
        return 0
    except (OSError, ValueError) as exc:
        print(f"연결 중단: {exc}\n기존 내용은 강제로 덮어쓰지 않습니다. 적용 중 오류라면 출력된 경로를 확인하세요.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
