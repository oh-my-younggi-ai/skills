# product-planning — Benchmark Trajectory

흐릿한 아이디어 → 기획 문서 3종(브리프/화면·플로우/로드맵) 스킬. iter별 전체 기록은 링크 참조.
측정 정의는 [METRICS.md](./METRICS.md), 채점기는 [grader.py](./grader.py) (전부 결정론적).

| Iter | Date | Change | Comparison | Floor | 핵심 지표 Δ | Record |
|------|------|--------|------------|-------|-------------|--------|
| 01 | 2026-07-14 | initial draft | vs no-skill | 18/18 green | 빈상태 0.32→0.78 · Phase근거 0→1.00 · 미해결 0.67→0 · 1.63× tokens | [iter-01](./iter-01-initial.md) |

> **iter-01 caveat:** M2(Phase 근거율)는 형식 결합 지표 — baseline 0은 산문으로 쓴 근거를
> 헤더 계약이 없어 못 잡은 것. baseline도 기획 통찰 자체는 강하며, 스킬의 실측 가치는
> **케이스 간 일관성**(baseline 편차 ±58%p vs 스킬 0%p)과 디자인 입력 형식 고정이다.

## Eval set

3 cases — `product-planning/evals/evals.json`이 정본:

1. **cold-start-two-sided** — 러닝 크루 매칭 (양면 시장, 시딩 필요). 로드맵이 콜드스타트에서 도출되는지.
2. **seo-single-player** — 면접 답변 뼈대 사이트 (검색 유입 도구형). SEO·콘텐츠 시딩이 Phase 1에 오는지.
3. **very-vague-idea** — 극흐릿 아이디어 + "모르겠다" 연발. 가설 제안 동작.

## Comparison strategy

- **iter-01:** vs no-skill — 절대 가치 확립.
- **iter-02+:** vs 이전 버전 (회귀 가드). 주기적으로 no-skill 재측정.
