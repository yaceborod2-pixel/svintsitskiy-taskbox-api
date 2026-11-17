from fastapi import FastAPI
from app.routers.health import healthRouter

app = FastAPI(title="TaskboxAPI")

app.include_router(healthRouter)
