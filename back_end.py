
from pydantic import BaseModel
from typing import List

# 1. Setup Pydantic Model (Schema Validation)
class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    msessages: List[str]


