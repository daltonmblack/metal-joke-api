from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from joke_generator import JokeGenerator

# from tourscraperapi.joke_generator import JokeGenerator

app = FastAPI()

jokeGenerator = JokeGenerator()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}

@app.get("/random_joke")
def read_joke():
  joke = jokeGenerator.get_random_joke()
  return {"joke": joke}

def start():
  """Launched with `poetry run start` at root level"""
  uvicorn.run("tourscraperapi.main:app", host="0.0.0.0", port=8000, reload=True)
