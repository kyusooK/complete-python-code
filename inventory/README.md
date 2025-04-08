# Inventory Sample Project

이 프로젝트는 Python과 SQLAlchemy ORM을 사용한 Inventory 애플리케이션입니다.

## 프로젝트 구조

```
inventory/
├── app/                # 애플리케이션 관련 코드
│   ├── __init__.py
│   └── main.py
├── config/             # 설정 파일
│   ├── __init__.py
│   └── database.py
├── models/             # 데이터베이스 모델 정의
│   ├── __init__.py
│   ├── base.py
│   └── inventory.py
├── repositories/       # 데이터 접근 계층
│   ├── __init__.py
│   └── inventory_repository.py
├── services/           # 비즈니스 로직 계층
│   ├── __init__.py
│   └── inventory_service.py
├── tests/              # 테스트 코드
│   ├── __init__.py
│   └── test_inventory.py
├── .env                # 환경 변수 파일 (개발용)
├── alembic.ini         # Alembic 마이그레이션 설정
├── requirements.txt    # 의존성 패키지
└── README.md           # 프로젝트 설명
```

## 설치 방법

1. 가상 환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # 리눅스/맥
venv\Scripts\activate     # 윈도우
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정
```bash
cp .env.example .env
# .env 파일 수정
```

4. 데이터베이스 마이그레이션
```bash
alembic upgrade head
```

5. 애플리케이션 실행
```bash
python -m app.main
```

## 프로젝트 설명

이 프로젝트는 SQLAlchemy ORM을 사용하여 inventory 정보를 관리하는 애플리케이션입니다.
- 레이어드 아키텍처(Layered Architecture) 패턴 적용
- SQLAlchemy ORM을 사용한 데이터베이스 액세스
- Alembic을 사용한 데이터베이스 마이그레이션 관리
