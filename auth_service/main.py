from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.post("/verify")
async def verify(request: Request):
    apiKey = request.headers.get("X-Api-Key")
    if not apiKey:
        raise HTTPException(status_code=400, detail="X-Api-Key header missing")

    if apiKey == "thisiscool":
        return {"authorized": True}

    raise HTTPException(status_code=401, detail="Unauthorized")
