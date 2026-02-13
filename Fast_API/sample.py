from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PostData(BaseModel):
    title: str
    body: str
    userId: int

@app.post(
    "/posts",
    responses={
        400: {"description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    }
)
def create_post(data: PostData):

    if data.userId <= 0:
        raise HTTPException(status_code=400, detail="Invalid userId")

    try:
        return {
            "message": "Post created",
            "data": data
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong")
