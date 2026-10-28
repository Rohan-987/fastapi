from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Welcome to FastAPI Blog</h1>"

@app.get("/about")
def about():
    return {"project": "FastAPI Blog", "status": "Running"}