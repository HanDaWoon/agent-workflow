# Claude Code·Codex 설치

일반 사용은 네이티브 플러그인 설치를 권장한다. 두 호스트가 같은 `engineering-workflow` 원본을 사용하며, 선택한 호스트에만 설치할 수 있다. Matt 스킬·Orca·에이전트 프로그램은 별도로 준비한다.

## 로컬 checkout에서 설치

checkout의 절대 경로로 marketplace를 등록한 뒤 플러그인을 설치한다. 아래 `/path/to/agent-workflow`를 실제 checkout 경로로 바꾼다.

```bash
# Codex
codex plugin marketplace add /path/to/agent-workflow
codex plugin add agent-workflow@agent-workflow

# Claude Code
claude plugin marketplace add /path/to/agent-workflow
claude plugin install agent-workflow@agent-workflow --scope user
```

필요한 호스트의 명령만 실행한다. 둘 모두 필요하면 두 묶음을 실행한다. Codex는 현재 CLI의 사용자 플러그인 설정에, Claude는 위의 명시적인 `user` 범위에 설치한다. Claude를 특정 프로젝트에만 적용하려면 그 프로젝트에서 `--scope project` 또는 개인 로컬 설정인 `--scope local`을 선택한다. 프로젝트 범위는 그 프로젝트의 설정 파일을 변경한다.

## GitHub에서 설치

checkout이나 Python 없이 다음 명령을 사용한다.

```bash
# Codex
codex plugin marketplace add HanDaWoon/agent-workflow
codex plugin add agent-workflow@agent-workflow

# Claude Code
claude plugin marketplace add HanDaWoon/agent-workflow
claude plugin install agent-workflow@agent-workflow --scope user
```

이미 같은 이름의 로컬 marketplace가 등록되어 있다면 먼저 플러그인과 marketplace를 아래 제거 명령으로 해제한 뒤 GitHub source를 등록한다. 같은 이름의 source를 추가하는 것이 자동 전환이라고 가정하지 않는다.

## 사용과 적용 확인

설치 후 **새 세션**을 시작한다. 작업 요청의 내용에 따라 호스트가 스킬을 선택한다. 확실하게 적용하려면 다음처럼 명시적으로 호출한다.

- Codex: `$agent-workflow:engineering-workflow`를 선택하고 작업 요청을 입력한다.
- Claude Code: `/agent-workflow:engineering-workflow` 뒤에 작업 요청을 입력한다.

예: `engineering-workflow로 이 프로젝트의 다음 구현 작업을 계획해줘.` 설치 목록은 `codex plugin list --json` 또는 `claude plugin list --json`으로 확인한다. 실제 사용 시 스킬 본문과 필요한 reference를 읽었는지도 확인한다. 단순 질문에는 전체 구현 절차가 필요하지 않다.

플러그인 설치는 프로젝트의 AGENTS·CLAUDE 내용을 강제로 바꾸지 않는다. 플러그인 루트의 CLAUDE.md도 프로젝트 지침으로 로딩되지 않는다. 모든 자연어 요청에서 자동 선택을 보장하는 설정과 설치 여부는 구분한다. 플러그인으로 전환할 때는 승인된 프로젝트 범위에서 기존 직접 연결과 관리 블록을 함께 검토해 두 버전이 경쟁하지 않게 한다. 자동 제거·일괄 전환은 제공하지 않는다.

## 갱신과 제거

GitHub source를 등록한 경우 marketplace를 먼저 갱신한 뒤 설치 버전을 갱신한다. 로컬 source는 해당 checkout을 갱신한 뒤 플러그인을 다시 설치한다. 패키지 내용을 배포할 때 두 plugin manifest의 버전을 함께 올린다. 이미 실행 중인 세션 대신 새 세션에서 확인한다.

```bash
# Codex: GitHub source 갱신 후 재설치
codex plugin marketplace upgrade agent-workflow
codex plugin add agent-workflow@agent-workflow

# Claude Code: GitHub source 갱신 후 업데이트
claude plugin marketplace update agent-workflow
claude plugin update agent-workflow@agent-workflow --scope user
```

제거하려면 설치한 범위와 동일하게 실행한다. 다른 플러그인이나 Matt·Orca는 대상이 아니다.

```bash
codex plugin remove agent-workflow@agent-workflow
codex plugin marketplace remove agent-workflow

claude plugin uninstall agent-workflow@agent-workflow --scope user
claude plugin marketplace remove agent-workflow
```

Claude는 제거한 버전의 캐시를 즉시 모두 지우지 않을 수 있다. 캐시 존재만으로 활성 설치라고 판단하지 말고 설치 목록과 새 세션을 확인한다.

## 패키지 구조와 호환 경로

실제 배포 단위는 `plugins/agent-workflow/`다. 호스트별 manifest와 공통 `skills/engineering-workflow/`만 포함하며 references·한국어 보고 assets까지 패키지 안에서 완결된다. marketplace는 호스트별 JSON을 사용하고 스킬 본문은 복제하지 않는다. 설치 캐시에 `.scratch`, Git 이력 또는 개발 도구를 넣지 않는다.

저장소 루트의 `skills/`는 `plugins/agent-workflow/skills`로 향하는 상대 심볼릭 링크다. 기존 Linux 프로젝트의 절대 원본 포인터와 연결 블록을 유지하기 위한 경로다. 네이티브 플러그인은 이 링크를 사용하지 않는다. Windows에서 호환 링크가 일반 파일로 checkout되면 아래 개발용 연결을 쓰기 전에 Git의 심볼릭 링크 지원을 확인한다.

형식과 사용 근거: [OpenAI Build plugins](https://learn.chatgpt.com/docs/build-plugins), [Claude plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [Claude plugins reference](https://code.claude.com/docs/en/plugins-reference). 명령 예시는 Codex 0.154.0·Claude Code 2.1.268 형식을 따른다.

## 개발용: 원본을 프로젝트에 직접 연결

이 저장소를 유지할 위치에 둔 뒤 Python 3으로 실행한다. 아래 `/path/to/project`는 연결할 Git 프로젝트 루트로 바꾼다.

```bash
python3 scripts/connect.py --project /path/to/project --agent codex
python3 scripts/connect.py --project /path/to/project --agent claude
python3 scripts/connect.py --project /path/to/project --agent both
```

세 명령 중 필요한 하나를 선택한다. 기본 실행은 파일 diff와 링크 대상을 보여주는 미리보기다. 확인한 명령에 `--apply`를 추가하면 적용한다.

```bash
python3 scripts/connect.py --project /path/to/project --agent both --apply
```

| 선택 | 스킬 연결 위치 | 자동 진입 지침 |
| --- | --- | --- |
| `codex` | `.agents/skills/engineering-workflow` | `AGENTS.md`에 조건부 원본 읽기 추가 |
| `claude` | `.claude/skills/engineering-workflow` | `CLAUDE.md`에 조건부 원본 읽기 추가. 기존 AGENTS가 있으면 함께 import |
| `both` | 위 두 위치 | 두 진입 파일에서 같은 원본 사용. 두 에이전트를 자동으로 실행하지 않음 |

연결 대상 디렉터리는 실제 스킬 원본을 가리키는 심볼릭 링크다. 진입 지침에는 원본의 실제 절대 경로를 기록해 검색 도구가 링크를 생략해도 직접 읽도록 한다. 원본 수정은 다음 읽기부터 반영되므로 원본 저장소를 이동·삭제하면 연결이 끊어진다. 다른 호스트에 프로젝트만 복제해도 해당 원본 경로가 자동 준비되지는 않는다. 심볼릭 링크 생성이 허용되지 않는 호스트는 오류를 보고한다. Windows에서 개발용 연결을 사용하려면 심볼릭 링크 생성 권한이 필요하다.

기존 지침은 보존하고 `agent-workflow:begin`과 `agent-workflow:end` 사이에 연결 지침을 추가한다. 같은 연결을 반복해도 중복으로 추가하지 않는다. 다른 내용의 기존 스킬 경로, 수정된 관리 블록, 기존 workflow 지침, 외부로 향하는 심볼릭 링크 경유 경로가 있으면 자동 병합하지 않는다. 원래 파일을 검토하고 [프로젝트 템플릿](../templates/project-workflow.md)의 진입 조건을 기존 지침에 연결한다. 선택은 추가할 호스트 범위이며, `both` 사용 후 `codex`를 선택해도 Claude 연결을 삭제하지 않는다.

하드링크로 공유된 지침도 자동 변경하지 않는다. Codex 연결 시 루트 `AGENTS.override.md`가 있으면 새 AGENTS가 무시될 수 있어 자동 연결을 중단한다. 기존 우선 지침에 진입 조건을 직접 병합하고 새 세션에서 실제 적용을 확인한다.

실행 중 같은 지침을 다른 프로세스가 편집하지 않도록 한다. 알려진 충돌은 쓰기 전에 검사하지만 여러 파일을 하나의 트랜잭션으로 변경하는 도구는 아니다. 디스크·권한 오류가 적용 도중 발생하면 출력된 적용 경로를 확인하고 원인을 해결한 뒤 같은 명령으로 재확인한다. 강제 덮어쓰기·자동 삭제·전역 설치 기능은 제공하지 않는다.

## 기존 직접 연결에서 전환

기존 AGENTS·CLAUDE에 원본 포인터가 있으면 먼저 해당 진입 지침과 심볼릭 링크를 확인한다. 같은 호스트에 플러그인과 직접 연결이 함께 있으면 두 버전이 경쟁할 수 있다. 허용된 프로젝트 변경 범위에서 기존 지침을 보존하며 하나의 진입 방식으로 정리한다. 연결 도구는 자동 전환이나 기존 연결 삭제를 수행하지 않는다.

공유 지침이 AGENTS.md에 있다면 Claude Code의 CLAUDE.md에서 `@AGENTS.md`로 import할 수 있다.

## 개발용 연결의 호환성 확인

위 Python 도구로 연결한 뒤 새 세션에서 일반 구현·재개·계획 요청을 보내 실제 원본 읽기를 확인한다. 단순 질문은 필요한 근거로 바로 답해야 한다. 명시적으로 호출할 때는 Codex의 `$engineering-workflow`, Claude Code의 `/engineering-workflow`를 사용할 수 있으나, 연결된 스킬의 자동 선택과 프로젝트 지침의 진입은 별도로 확인한다. 기본 읽기 위치와 스킬 형식은 [Codex 스킬 문서](https://learn.chatgpt.com/docs/build-skills), [Claude Code 스킬 문서](https://code.claude.com/docs/en/skills), [Claude의 AGENTS import 문서](https://code.claude.com/docs/en/memory#agentsmd)를 근거로 삼았다.

모델·effort는 선택한 호스트의 지원값과 실제 적용값으로 기록한다. 같은 `medium` 이름이 같은 추론량이라는 뜻은 아니다. 한 호스트에 설치한 Matt·Orca 스킬이 다른 호스트에서도 보인다고 가정하지 않으며, 필요한 기능이 없으면 설치를 시작하지 않고 제한을 보고한다. Orca 감독·리뷰·정리도 그 호스트에서 제공되는 계약을 사용한다.
