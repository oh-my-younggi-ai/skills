# product-planning — iter-01: initial draft

- **Date:** 2026-07-14
- **Skill commit:** 644e7c6
- **Comparison:** `with_skill` vs `no_skill`
- **Eval set:** 3 cases (cold-start-two-sided / seo-single-player / very-vague-idea)
- **Runner model:** claude-fable-5

## What changed this iteration

- 최초 버전. 가설: 5단계 워크플로우(intake→discovery 4스테이지→product-shape→roadmap→write-docs)가
  ① 산출물 구조를 계약 수준으로 고정하고 ② 화면 빈 상태(콜드스타트 화면)와
  ③ 도메인 역학 기반 Phase 근거를 베이스라인보다 안정적으로 만들 것.

## Headline result

> floor 18/18 green (3/3 케이스에서 문서 3종 계약 완전 준수) · 빈 상태 커버리지 0.32 → 0.78 ·
> Phase 도메인 근거율 0 → 1.00 · 미해결 표기 0.67 → 0건 · 비용 1.63× tokens.

## Quantitative results

### 회귀 바닥 (with_skill 전용 계약)

| Floor | Pass |
|---|---|
| F1 docs_exist / F2 transcript / F3 brief_sections / F4 product_sections / F5 phase_count / F6 no_placeholder | **18/18 green** (6종 × 3케이스) |

### 진행 지표 (with vs without, 3케이스 평균)

| 지표 | baseline | with_skill | Δ |
|---|---|---|---|
| M1 empty_state_coverage | 0.32 | 0.78 | ▲ +0.46 |
| M2 phase_rationale_rate | 0.00 | 1.00 | ▲ (형식 결합 — 아래 주의) |
| M3 nondev_task_hits (avg) | 1.0 | 2.0 | ▲ |
| M4 unresolved_unknowns (avg) | 0.67 | 0.00 | ▲ (0 목표) |
| M5 token_ratio | 1.00× | 1.63× | 비용 |
| duration (avg) | 174.5s | 391.8s | 2.25× |

집계기 기준 pass rate는 with 1.00 vs without 0.67 (+0.33)이지만, **baseline은 M4 1개
어설션만 채점되므로 이 델타는 동일 조건 비교가 아니다.** 신호는 위 지표 델타로 읽는다.

## Qualitative findings

- **측정 도구 버그를 iter 중 발견·수정.** M1 정규식이 "크루 0개/신청 0건/크루 없음"을
  못 잡아 0.2로 undercount → 보정 후 0.6 (SCPC 사례 3 "측정 도구의 거짓말" 재현.
  결과가 이상하면 파이프라인부터 의심).
- **M2는 형식 결합 지표다.** baseline 0은 근거가 없어서가 아니라 `## Phase` 헤더
  계약이 없어서다 (eval-1 baseline은 산문으로 훌륭한 SEO 근거를 씀). M2는 "근거가
  기계 판독 가능한 위치에 있는가"로 읽을 것. iter-02에서 산문 근거 검출 보완 후보.
- **baseline(Fable)은 기획 자체를 꽤 잘한다.** eval-1 baseline은 콘텐츠 제품 규정,
  SEO 체크리스트까지 스킬보다 깊었다 (nondev 3 > 2). 스킬의 실측 가치는 통찰이
  아니라 **일관성**: 3/3 케이스에서 같은 구조·빈 상태·근거가 보장되는 것, 그리고
  다음 단계(UI 디자인) 입력 형식이 고정되는 것.
- eval-0 baseline은 단일 문서 + 미해결 표기 2건 잔존 — 케이스 간 편차가 큼
  (baseline 표준편차 58%p가 그 증거).
- 대화 규율(질문 턴 종료, 스테이지당 ≤3질문, 승인 후 저장, "모르겠다"→가설 제안)은
  transcript상 3/3 준수 — 단 시뮬레이션 환경이므로 실사용 검증 필요.

## Decision → next iteration

- eval 확장: 차별점 압박 케이스(기존 대안이 압도적으로 강함), B2B 양면 페르소나 추가.
- M2 보완: 헤더 계약 밖 산문 근거도 잡는 측정식 검토.
- 실사용 1회(다음 실제 프로젝트 기획) 후 transcript 기반으로 질문 피로도(라운드 수) 확인.
