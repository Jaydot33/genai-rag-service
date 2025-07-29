from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    question: str
    document_id: str

class QueryResponse(BaseModel):
    answer: str
    context: List[str]
