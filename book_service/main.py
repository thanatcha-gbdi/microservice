from fastapi import FastAPI, HTTPException, Request
import requests

app = FastAPI(root_path="/books")

mocked_data = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

@app.get("/")
async def read_books(request: Request):
    q = request.headers.get("X-Api-Key")
    if q:
        response = requests.post("http://auth_service:80/verify", headers={"X-Api-Key": q})
        if response.status_code == 200:
            return {"data": mocked_data}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        raise HTTPException(status_code=400, detail="No API key provided")
