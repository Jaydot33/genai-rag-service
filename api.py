from fastapi import APIRouter
from app.models import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    # Placeholder: actual RAG logic goes here soon
    return QueryResponse(answer="Coming soon!", context=[])
