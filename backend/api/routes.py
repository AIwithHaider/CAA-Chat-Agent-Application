# We will define all the routes here, in this way our main.py remains clean
from fastapi import APIRouter
from backend.tools.search_tool import get_response
from backend.api.schemas import RequestState


router = APIRouter()

@router.post("/chat")
def chat(request: RequestState):
    provider = request.provider
    model = request.model
    system_prompt = request.system_prompt
    query = request.messages

    response = get_response(system_prompt, query, provider, model)
    return response


