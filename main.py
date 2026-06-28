from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://dhruvrb2005_db_user:123456dhruv@cluster0.ujeeogf.mongodb.net/notes")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    docs = conn.notes.notes.find_one({})
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}