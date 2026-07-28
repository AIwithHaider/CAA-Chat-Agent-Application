from fastapi import FastAPI
from backend.api.routes import router

# 2. Setup AI Agent from FrontEnd Request
app = FastAPI(title="CAA-Chat Agent Application")


app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the CAA-Chat Agent Application!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)