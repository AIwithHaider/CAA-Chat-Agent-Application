from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response

# 1. Setup Pydantic Model (Schema Validation)
class RequestState(BaseModel):
    system_prompt: str
    messages: List[str]

# 2. Setup AI Agent from FrontEnd Request
app = FastAPI(title="CAA-Chat Agent Application")

@app.post("/chat")
def chat(request: RequestState):
    system_prompt = request.system_prompt
    query = request.messages

    response = get_response(system_prompt, query)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
