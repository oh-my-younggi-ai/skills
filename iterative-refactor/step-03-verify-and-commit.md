# Step 3: 테스트 검증 → 사용자 리뷰 → 커밋

## RULES

- 테스트가 실패한 상태에서 사용자 승인 단계로 절대 넘어가지 않는다.
- 커밋은 반드시 사용자 [A] 승인 후에만 생성한다.
- 원격 push 금지.
- **EARLY EXIT** = 이 step을 즉시 중단하고 지정된 파일로 이동한다.


## INSTRUCTIONS

### 1. 테스트 실행

`{test_command}`를 실행한다.

**테스트 통과 시** → 단계 2로 진행.

**테스트 실패 시**:
- 실패한 테스트와 오류 메시지를 출력한다.
- 원인을 분석하고 수정한다.
- 수정 후 테스트를 다시 실행한다.
- 3회 시도 후에도 실패하면 HALT:

  > 테스트를 통과시키지 못했습니다. 실패 내용:
  > {실패 로그}
  >
  > `[F]` 직접 수정할게요 — 수정 완료 후 알려주시면 다시 테스트를 실행합니다.
  > `[S]` 이 배치 건너뛰기 — 미완료 상태로 다음 배치로 넘어갑니다.
  > `[X]` 작업 중단

  - **[F]**: 사용자가 알려주면 테스트를 다시 실행하고 단계 1로 돌아간다.
  - **[S]**: 단계 4의 `건너뛰기` 경로로 이동.
  - **[X]**: HALT. 현재 변경 사항은 커밋하지 않은 상태로 유지.


### 2. 변경 사항 요약 출력

테스트 통과 후 사용자에게 검토할 내용을 출력한다:

---

**배치 {current_batch_index + 1} 구현 완료** ✅

테스트 통과: {통과한 테스트 수}개

**변경된 파일:**
```
{git diff --name-only 출력}
```

**변경 요약:**
{파일별 주요 변경 내용을 간결하게 — 파일명:줄번호 형식}

**현재 배치 항목:**
- #{번호} {항목 제목}
- #{번호} {항목 제목}

---

> 코드를 검토한 뒤 아래 중 하나를 선택해 주세요:
>
> `[A]` 승인 — 커밋하고 다음 배치로 넘어갑니다.
> `[R]` 수정 요청 — 수정할 내용을 알려주세요. 수정 후 다시 테스트를 실행합니다.
> `[S]` 건너뛰기 — 이 배치를 커밋 없이 넘어갑니다 (변경 사항은 staged 상태로 유지).
> `[X]` 중단 — 작업을 멈추고 현재 상태를 유지합니다.

HALT하고 사용자 입력을 기다린다.


### 3. 사용자 입력 처리

#### [A] 승인

커밋 메시지를 생성한다.

`{commit_style}` 설정을 따른다:

- **conventional**: `{commit_type}({scope}): {subject}` 형식
  - `{commit_type}` = INITIALIZATION에서 로드한 값 (기본값 `refactor`)
  - `{scope}` = 주요 변경 패키지/모듈 이름 (예: `domain`, `service`, `dto`)
  - `{subject}` = 현재 배치 항목들의 핵심 내용 요약 (50자 이내, 영문 소문자, 명령형)
- **simple**: 배치 제목을 그대로 사용

커밋 실행:
```bash
git add {변경된 파일들} {task_file}
git commit -m "..."
```

커밋 완료 후:
> ✅ 커밋 완료: `{커밋 해시}` — {커밋 메시지}

`{progress_file}`을 업데이트한다:
- 해당 배치 섹션 상태를 `🔄 진행 중` → `✅`로 변경
- 배치 섹션 아래에 커밋 정보 추가: `> 커밋: \`{커밋 해시}\` · {현재 날짜 YYYY-MM-DD HH:MM}`
- frontmatter의 `current_batch_index` += 1
- frontmatter의 `updated_at`을 현재 시각으로 갱신
- body 상단 진행률 요약 갱신: `완료: {완료 수}/{총 배치 수}`

`{current_batch_index}` += 1

**컨벤션 후보 확인**

`{shared_conventions_dir}/CONTRIBUTING.md`의 판단 기준에 따라 이번 배치에서 컨벤션 후보가 있는지 검토한다.

- 후보가 없으면 건너뛴다 (질문하지 않음).
- 후보가 있으면 `{shared_conventions_dir}/CONTRIBUTING.md`의 제안 형식으로 출력하고 HALT한다.
  - **[Y]**: `{shared_conventions_dir}/CONTRIBUTING.md`의 추가 절차에 따라 반영하고, `{code_conventions}`에도 추가한다.
  - **[N]**: 건너뛴다.

**EARLY EXIT** → `./step-02-implement-batch.md`

#### [R] 수정 요청

사용자의 수정 요청을 반영한다.
수정 완료 후 단계 1 (테스트 실행)로 돌아간다.

#### [S] 건너뛰기

`{progress_file}`을 업데이트한다:
- 해당 배치 섹션 상태를 `🔄 진행 중` → `⏸ 건너뜀`으로 변경
- frontmatter의 `current_batch_index` += 1
- frontmatter의 `updated_at`을 현재 시각으로 갱신

`{current_batch_index}` += 1

> 배치 {current_batch_index}을 건너뛰었습니다.
> (변경 사항이 있다면 unstaged 상태로 유지됩니다)

**EARLY EXIT** → `./step-02-implement-batch.md`

#### [X] 중단

> 작업을 중단합니다. 현재 변경 사항은 커밋되지 않은 상태입니다.
> 이어서 작업하려면 `/iterative-refactor`를 다시 실행하세요.

`{progress_file}`의 `🔄 진행 중` 상태는 그대로 유지한다 (재개 감지에 사용됨).

HALT.
