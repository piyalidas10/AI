from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from app.routes import upload, chat

app = FastAPI(title="Enterprise RAG API")

templates = Jinja2Templates(directory="app/templates")

app.include_router(upload.router)
app.include_router(chat.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )


@app.get("/health")
async def health():
    return {"status": "ok"}