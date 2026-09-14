# Agent Workflow

Codex와 Claude Code에서 함께 사용하는 이슈 기반 코딩 워크플로우 플러그인입니다. 구현·계획·재개 요청을 검증, 리뷰, 커밋, 통합, 완료 자원 정리까지 연결합니다.

## 설치

사용할 호스트의 두 명령을 실행하고 새 세션을 시작합니다.

**Codex**

```bash
codex plugin marketplace add HanDaWoon/agent-workflow
codex plugin add agent-workflow@agent-workflow
```

**Claude Code**

```bash
claude plugin marketplace add HanDaWoon/agent-workflow
claude plugin install agent-workflow@agent-workflow --scope user
```

두 호스트에서 사용하려면 두 묶음을 모두 실행합니다. Matt Pocock 스킬과 Orca는 별도로 준비하며 이 플러그인이 설치하거나 업데이트하지 않습니다.

## 사용

- Codex: `$agent-workflow:engineering-workflow`와 작업 요청을 입력합니다.
- Claude Code: `/agent-workflow:engineering-workflow` 뒤에 작업 요청을 입력합니다.

예: `이 프로젝트의 다음 구현 작업을 계획해줘.`

작업 내용에 따른 자동 선택은 호스트와 프로젝트 지침에 따릅니다. 확실하게 적용하려면 스킬을 명시적으로 호출합니다. 단순 질문에는 전체 구현 절차를 적용하지 않습니다.

## 동작 방식

- GitHub 이슈로 작업 범위와 수용 기준을 연결합니다.
- 단일 실행을 기본으로 하며, 감독 실행에서는 Orca가 작업자와 이슈별 워크트리를 관리합니다.
- 변경 영향에 맞는 모델·effort와 검증·리뷰 강도를 선택합니다.
- 구현, 통합, 배포의 실제 상태를 구분하고 정리 가능한 터미널·워크트리를 제거합니다.
- 공통 스킬은 실행 절차를, 프로젝트 설정은 테스트 명령·기준 브랜치·허용 범위를 소유합니다.

## 안내

- [설치·업데이트·제거](docs/agent-setup.md)
- [워크플로우 구조와 기본값](docs/workflow.md)
- [실행 스킬](plugins/agent-workflow/skills/engineering-workflow/SKILL.md)
- [전역 진입 템플릿](templates/global-entry.md) · [프로젝트 설정 템플릿](templates/project-workflow.md)
- [이슈 템플릿](plugins/agent-workflow/skills/engineering-workflow/assets/issue.md) · [완료 보고 템플릿](plugins/agent-workflow/skills/engineering-workflow/assets/completion-report.md)

에이전트용 지침은 영어, 사용자 안내와 이슈·완료 보고 템플릿은 한국어로 제공합니다.
