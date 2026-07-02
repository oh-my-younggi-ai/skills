# Step 2: 현재 배치 구현

## RULES

- 구현 중 커밋 금지. 커밋은 step-03에서만 생성한다.
- 원격 push 금지.
- INITIALIZATION에서 로드한 `{code_conventions}`을 구현 전에 반드시 반영한다.
- 현재 배치 항목 외의 리팩토링을 범위 없이 확장하지 않는다. 발견한 문제는 메모 후 사용자에게 알린다.
- **EARLY EXIT** = 이 step을 즉시 중단하고 지정된 파일로 이동한다.


## PRECONDITION

`{groups}`와 `{current_batch_index}`가 설정되어 있는지 확인한다.
`{current_batch_index}`가 `{groups}` 길이 이상이면 → 모든 배치 완료.

> 🎉 모든 배치를 완료했습니다!
> `{task_file}`의 모든 항목이 처리되었습니다.

HALT하고 종료한다.


## INSTRUCTIONS

### 1. 현재 배치 설정

`{current_batch}` = `{groups}[{current_batch_index}]`

총 배치 수와 현재 위치를 출력한다:

> **배치 {current_batch_index + 1} / {total_batches}** — {배치 제목}
> 항목: {항목 목록}
> 시작합니다.

`{baseline_commit}` = 현재 HEAD 커밋 해시 (`git rev-parse HEAD`)
버전 관리가 없으면 `NO_VCS`로 설정.

`{progress_file}`의 해당 배치 섹션 상태를 `⏳` → `🔄 진행 중`으로, frontmatter의 `updated_at`을 현재 시각으로 업데이트한다.


### 2. 코드 컨벤션 적용

INITIALIZATION에서 로드한 `{code_conventions}`을 구현 가이드로 사용한다.


### 3. 코드베이스 조사

현재 배치의 항목들과 관련된 파일, 클래스, 메서드를 파악한다.

- 영향 범위 (수정할 파일 목록)
- 의존 관계 (수정 순서)
- 현재 구조와 목표 구조의 차이

조사 결과를 간략히 출력한다 (파일 경로, 주요 변경 내용 요약).


### 4. 구현

항목을 하나씩 구현한다. 의존 관계가 있으면 의존 대상을 먼저 처리한다.

구현 중:
- 테스트 파일도 함께 수정/추가한다 (기존 테스트가 깨지지 않게).
- `{code_conventions}`을 따른다.
- `{auto_format}`이 true인 경우 `{format_command}`를 실행한다.

각 항목 구현 완료 시 한 줄로 보고:
> ✓ #{번호} {항목 제목} — {변경된 파일 수}개 파일 수정


### 5. 구현 완료 확인

모든 항목 구현 후:

- 변경된 파일 목록을 출력한다 (`git diff --name-only`).
- 빌드가 통과하는지 컴파일만 먼저 확인한다 (가능한 경우: `./gradlew compileJava` 등).
- 컴파일 오류가 있으면 즉시 수정한 뒤 다시 확인한다.
- `{task_file}`의 현재 배치 항목들을 `- [ ]` → `- [x]`로 업데이트한다.


## NEXT

Read fully and follow `./step-03-verify-and-commit.md`