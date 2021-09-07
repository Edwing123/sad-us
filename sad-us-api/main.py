from fastapi import FastAPI
from fastapi.params import Query

from models import Thought


app = FastAPI()


# upload a thought
@app.post("/add-thought")
def add_thought(thought: Thought):
    return {"title": thought.title}


# get thoughts
@app.get("/get-thoughts")
def get_thoughts():
    return {"thoughts": []}
