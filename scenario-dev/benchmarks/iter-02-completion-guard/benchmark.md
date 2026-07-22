# Skill Benchmark: scenario-dev

**Model**: unavailable
**Date**: 2026-07-22T05:38:30Z
**Evals**: 4 (1 run per configuration)

## Summary

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% ± 0% | 33% ± 0% | +0.67 |
| Time | 0.0s ± 0.0s | 0.0s ± 0.0s | +0.0s |
| Tokens | 0 ± 0 | 0 ± 0 | +0 |

## Notes

- 수정본은 세 완료 증거 단언을 모두 통과했고, 기준선은 수동 시나리오 식별자를
  남기지 않아 새 lint에서 실패했다.
- 수동 walkthrough fixture 하나의 paired run이므로 일반적인 pass rate 추정이 아니다.
- 실행 환경이 신뢰할 수 있는 토큰과 소요 시간 값을 제공하지 않아 효율 비교는 하지
  않는다.
- goal 호환은 Codex adapter 정책이며 도구 중립적인 scenario-dev benchmark에는 넣지
  않았다.
