from fastapi import FastAPI
from backend.tools.search_tool import get_response
from backend.config.settings import RequestState

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