from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
import uvicorn
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from api import tic_tac_toe

app = FastAPI(title="Tic Tac Toe Web App")
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/game/new", response_model=tic_tac_toe.GameState)
async def new_game():
    return tic_tac_toe.new_game()

@app.post("/api/game/move", response_model=tic_tac_toe.GameState)
async def make_move(move: tic_tac_toe.Move):
    return tic_tac_toe.make_move(move)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
