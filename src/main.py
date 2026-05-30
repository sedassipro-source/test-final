from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import engine, Base
import os

from src.routers import auth as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="test-final",
    description="A FastAPI + PostgreSQL project: test-final",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    app.include_router(auth_router.router, prefix="/auth", tags=["auth"])


@app.get("/health")
async def health():
    return {"status": "ok", "service": "test-final"}
