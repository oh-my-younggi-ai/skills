---
shared_conventions_dir: '~/.config/ai-rules/conventions'
settings_file: './settings.md'
---

# Iterative Refactor Workflow

**Goal:** 리팩토링 체크리스트를 읽고, 항목을 묶어 하나씩 구현한 뒤 테스트 통과 → 사용자 승인 → 커밋 순서로 안전하게 진행한다.

**CRITICAL:** step 파일을 순서대로 읽고 따른다. 동시에 여러 step을 로드하지 않는다.


## 경로 규칙

- `~/.config/ai-rules/...`로 시작하는 경로 (`shared_conventions_dir`, `settings_file`): 사용자 홈 디렉토리 기준 절대 경로. 도구 중립 경로이며 Claude Code·Codex 어디서 실행하든 동일하게 해석된다. 모든 프로젝트가 공유하는 전역 설정이며, 현재 작업 디렉토리와 무관하다.
- `{project_root}`로 시작하는 경로 (`{progression_dir}` 등): 스킬을 실행한 프로젝트 루트(현재 작업 디렉토리) 기준. 프로젝트마다 별도로 생성된다.


## INVARIANTS (예외 없음)

- 모든 출력은 한국어로 한다 (`{communication_language}`로 재정의 가능).
- 커밋은 반드시 사용자 [A] 승인 이후에만 생성한다. 자동 커밋 금지.
- 테스트가 실패한 상태에서 사용자 승인 단계로 넘어가지 않는다.
- 원격 push 금지 — 로컬 커밋만.
- 공유 컨벤션과 스킬 설정을 먼저 읽어 확인하고, 이후 step을 실행한다.


## STEP PROCESSING RULES

1. **READ COMPLETELY**: step 파일 전체를 읽은 뒤 실행한다.
2. **FOLLOW SEQUENCE**: 지정된 순서로만 실행한다.
3. **WAIT FOR INPUT**: 체크포인트에서 반드시 멈추고 사람을 기다린다.
4. **LOAD NEXT**: 현재 step에서 명시한 다음 파일로 이동한다.


## 세션 상태 변수 (런타임에 설정)

이 변수들은 스킬 실행 중 메모리에서 관리된다:

- `{project_root}` — 현재 작업 디렉토리 (스킬을 실행한 프로젝트의 루트, cwd)
- `{task_file}` — 선택된 리팩토링 체크리스트 파일 경로
- `{groups}` — 그룹화된 배치 목록 (배열)
- `{current_batch_index}` — 현재 진행 중인 배치 번호 (0-based)
- `{current_batch}` — 현재 배치의 항목 목록
- `{baseline_commit}` — 현재 배치 시작 시점의 HEAD commit
- `{progression_dir}` — progress 파일 저장 디렉토리: `{project_root}/progression/`
- `{progress_file}` — 현재 세션의 progress 파일 경로

### 컨벤션/설정 변수 (INITIALIZATION에서 로드)

- `{code_conventions}` — 적용할 코드 컨벤션 전문 (common.md + 스택별 파일)
- `{test_command}` — 테스트 실행 명령어
- `{communication_language}` — 출력 언어
- `{commit_style}` — 커밋 메시지 스타일
- `{commit_type}` — 커밋 타입
- `{auto_format}` — 구현 후 포매터 자동 실행 여부
- `{format_command}` — 포매터 실행 명령어
- `{grouping_strategy}` — 그룹화 전략 힌트

### `{progress_file}` 경로 계산 규칙

1. `{task_file}`의 basename에서 확장자 제거 → `{stem}`
2. `{progression_dir}/{stem}.progress.md`를 기본 경로로 사용
3. 해당 파일이 이미 존재하고 `task_file:` frontmatter가 다른 파일을 가리키면 (충돌):
   - 상위 디렉토리명을 접두사로 붙임: `{parent_dir}-{stem}.progress.md`


## INITIALIZATION

### 1. 공유 컨벤션 로드

`{shared_conventions_dir}/INDEX.md`를 읽고 안내에 따라 `common.md`와 프로젝트 스택에 맞는 파일을 읽어 `{code_conventions}`로 합쳐 보관한다.

### 2. 공유 설정 로드

`{shared_conventions_dir}/settings.md`를 읽어 `test_command`, `communication_language`, `commit_style`, `auto_format`, `format_command`의 기본값을 로드한다.

### 3. 스킬 설정 로드

`{settings_file}`을 읽어 `commit_type`, `grouping_strategy`를 로드한다. 1~2에서 로드한 키와 이름이 겹치면 `{settings_file}`의 값이 우선한다.

### 4. 첫 번째 Step 실행

Read fully and follow: `./step-01-select-and-group.md`