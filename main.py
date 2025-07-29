from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="GenAI RAG Service",
    description="Production-ready API for Retrieval-Augmented Generation with LLMs and vector DB",
    version="0.1.0",
)

app.include_router(router)
