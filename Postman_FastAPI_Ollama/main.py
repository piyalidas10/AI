from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import requests
from datetime import datetime

app = FastAPI()
class PromptRequest(BaseModel):
    prompt: str
    system: Optional[str] = "You are a helpful AI assistant."
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(default=0.9, ge=0.0, le=1.0)
    top_k: Optional[int] = Field(default=40, ge=1)

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
            "system": request.system,
            "stream": False,
            "options": {
                "temperature": request.temperature,
                "top_p": request.top_p,
                "top_k": request.top_k
            }
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
