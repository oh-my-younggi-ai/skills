# Iterative Refactor — 스킬 전용 설정

이 파일은 직접 수정해서 이 스킬만의 동작을 조정할 수 있습니다.
공통 설정은 `~/.config/ai-rules/conventions/settings.md`를 따르며, 여기서 같은 키를 정의하면 이 값이 우선합니다.

---

## 커밋 타입

```
commit_type: refactor
```

`commit_style: conventional`일 때 사용할 타입입니다.
작업 성격에 맞게 변경하세요.

예:
- `refactor` — 리팩토링 (기본값)
- `feat` — 새 기능 개발
- `fix` — 버그 수정
- `test` — 테스트 추가/수정
- `chore` — 설정, 빌드, 유지보수

---

## 그룹화 전략 힌트

```
grouping_strategy: dependency
```

리팩토링 항목을 묶는 기준입니다:
- `dependency` — 파일/클래스 의존성이 같은 것끼리 묶음 (기본값)
- `layer` — 레이어(도메인/서비스/컨트롤러) 기준으로 묶음
- `manual` — 자동 그룹화 없이, 항목별로 개별 실행 (느리지만 가장 안전)
