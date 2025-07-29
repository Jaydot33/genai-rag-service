from fastapi import APIRouter
from app.models import QueryRequest, QueryResponse
from app.vector_db import search_similar_documents
from app.llm_engine import generate_answer

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    contexts = search_similar_documents(request.question)
    answer = generate_answer(request.question, contexts)
    return QueryResponse(answer=answer, context=contexts)
