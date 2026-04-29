from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Kubernetes Project"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Alice"}
        ]
    }