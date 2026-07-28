# Before creating the API, let's define what data the client will send.

from pydantic import BaseModel
from typing import List

# Setup Pydantic Model (Schema Validation)
class RequestState(BaseModel):
    system_prompt: str
    messages: List[str]
