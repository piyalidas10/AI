from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from datetime import datetime

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {
        "success": True,
        "message": "API is running",
        "timestamp": datetime.utcnow()
    }

@app.post("/generate")
def generate_text(request: PromptRequest):
    try:
        ollama_url = "http://host.docker.internal:11434/api/generate"

        payload = {
            "model": "phi3",
            "prompt": request.prompt,
            "stream": False
        }

        response = requests.post(ollama_url, json=payload)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Ollama error")

        result = response.json()

        return {
            "success": True,
            "model": "phi3",
            "response": result.get("response"),
            "timestamp": datetime.utcnow()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
