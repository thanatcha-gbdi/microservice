from fastapi import FastAPI, HTTPException, Request
import requests

app = FastAPI(root_path="/movies")

mocked_data = [
    {"id": 1, "name": "Movie 1", "genre": "Action"},
    {"id": 2, "name": "Movie 2", "genre": "Adventure"},
]

@app.get("/")
async def read_movies(request: Request):
    q = request.headers.get("X-Api-Key")
    if q:
        response = requests.post("http://auth_service:80/verify", headers={"X-Api-Key": q})
        if response.status_code == 200:
            return {"data": mocked_data}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        raise HTTPException(status_code=400, detail="No API key provided")
