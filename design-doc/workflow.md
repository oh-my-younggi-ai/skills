---
shared_conventions_dir: '~/.config/ai-rules/conventions'
settings_file: './settings.md'
---

# Design Doc Workflow

**Goal:** 무엇을 만들고 싶은지 파악하고, 질문을 통해 배경/범위/요구사항 등을 수집한 뒤 설계 문서를 작성한다.

**CRITICAL:** step 파일을 순서대로 읽고 따른다. 동시에 여러 step을 로드하지 않는다.


## 경로 규칙

- `~/.config/ai-rules/...`로 시작하는 경로 (`shared_conventions_dir`, `settings_file`): 사용자 홈 디렉토리 기준 절대 경로. 도구 중립 경로이며 Claude Code·Codex 어디서 실행하든 동일하게 해석된다. 모든 프로젝트가 공유하는 전역 설정이며, 현재 작업 디렉토리와 무관하다.
- `{project_root}`로 시작하는 경로 (`{design_doc_path}` 등): 스킬을 실행한 프로젝트 루트(현재 작업 디렉토리) 기준. 프로젝트마다 별도로 생성된다.


## INVARIANTS (예외 없음)

- 모든 출력은 한국어로 한다 (`{communication_language}`로 재정의 가능).
- 설계 문서는 반드시 사용자 `[A]` 승인 이후에만 파일로 저장한다.
- 한 라운드에 너무 많은 질문을 쏟아내지 않는다 (라운드당 4~6개).
- 공유 설정과 스킬 설정을 먼저 읽어 확인하고, 이후 step을 실행한다.


## STEP PROCESSING RULES

1. **READ COMPLETELY**: step 파일 전체를 읽은 뒤 실행한다.
2. **FOLLOW SEQUENCE**: 지정된 순서로만 실행한다.
3. **WAIT FOR INPUT**: 체크포인트에서 반드시 멈추고 사람을 기다린다.
4. **LOAD NEXT**: 현재 step에서 명시한 다음 파일로 이동한다.


## 세션 상태 변수 (런타임에 설정)

- `{project_root}` — 현재 작업 디렉토리 (스킬을 실행한 프로젝트의 루트, cwd)
- `{topic}` — 사용자가 설계하고 싶은 대상의 한 줄 설명
- `{slug}` — 파일명에 사용할 kebab-case 식별자
- `{design_doc_path}` — 설계 문서 저장 경로
- `{qa_log}` — 카테고리별로 정리된 질문/답변 기록
- `{question_round}` — 현재 질문 라운드 번호 (1부터 시작)
- `{design_doc}` — 설계 문서 초안 내용

### 설정 변수 (INITIALIZATION에서 로드)

- `{communication_language}` — 출력 언어
- `{output_dir}` — 설계 문서 저장 디렉토리 (`{project_root}` 기준 상대 경로)
- `{max_question_rounds}` — 질문 라운드 최대 횟수


## INITIALIZATION

### 1. 공유 설정 로드

`{shared_conventions_dir}/settings.md`를 읽어 `communication_language`의 기본값을 로드한다.

### 2. 스킬 설정 로드

`{settings_file}`을 읽어 `output_dir`, `max_question_rounds`를 로드한다. 1에서 로드한 키와 이름이 겹치면 `{settings_file}`의 값이 우선한다.

### 3. 첫 번째 Step 실행

Read fully and follow: `./step-01-gather-topic.md`
