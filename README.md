# test-final

A FastAPI + PostgreSQL project: test-final

## Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL (async via SQLAlchemy)
- **Deploy**: railway
- **Auth**: JWT (python-jose + passlib)
- **Cache**: Redis

## Getting Started

```bash
cp .env.example .env
# Fill in DATABASE_URL and other variables

pip install -r requirements.txt
uvicorn src.main:app --reload
```

## API Endpoints

- `GET /health` — Health check
- `POST /auth/token` — Obtain JWT token


## Environment Variables

See `.env.example` for required variables.
