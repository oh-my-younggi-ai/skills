---
title: '권한 온보딩'
status: 'done'
test_command: 'true'
---

<frozen-after-approval reason="human-owned contract">

### S1: 권한 없이는 다음 단계로 가지 않는다

- **Verification:** auto

### S2: 실제 기기 권한 팝업을 완료하면 다음 단계로 간다

- **Verification:** manual - 시스템 팝업 관찰이 남아 있다.

</frozen-after-approval>

## Coverage Map

| Scenario | Verification | Status | Test | Implementation |
|----------|--------------|--------|------|----------------|
| S1 | auto | verified | `test.kt` | `implementation.kt` |
| S2 | manual | verified | walkthrough | `implementation.kt` |

## Verification Log

- 2026-07-22: 기기에서 권한 팝업을 승인하고 홈으로 이동했다.

## Scenario Traceability

| Scenario | Verified by | Implementation |
|----------|-------------|----------------|
| S1: 권한 없이는 다음 단계로 가지 않는다 | [`test.kt`](../../../../fixtures/test.kt#L1) ✓ | [`implementation.kt`](../../../../fixtures/implementation.kt#L1) |
| S2: 실제 기기 권한 팝업을 완료하면 다음 단계로 간다 | manual walkthrough (see Verification Log) | [`implementation.kt`](../../../../fixtures/implementation.kt#L1) |
