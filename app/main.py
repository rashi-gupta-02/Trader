from fastapi import FastAPI
from app.db.session import init_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"status": "API is running!"}
