import logging
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/query")
async def query(search: str):
    return {"search": search}

@app.get("/health")
async def health():
    return {"status": "ok"}
