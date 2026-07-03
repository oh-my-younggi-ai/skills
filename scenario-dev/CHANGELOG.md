# scenario-dev — Changelog

Full benchmark records: `./benchmarks/`

## iter-01 · 2026-06-15 — initial draft

**Pass rate:** 1.00 (20/20) vs baseline 0.50 · **Δ** +0.50 · **Token cost** ≈ 1.65×

- 스킬 첫 버전. step-file BDD 워크플로우 (capture → confirm → cover → verify → present + fast lane) 구현
- 구조적 어설션(scenario artifact, traceability, red-first)에서 baseline 대비 명확한 우위
- 행동적 커버리지(behavioral)는 Sonnet baseline과 동률 — eval set이 너무 쉬움
- **Next:** 더 어려운 eval 케이스 추가, 행동 커버리지를 실제로 측정할 어설션 보강
