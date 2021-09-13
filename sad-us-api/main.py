from typing import List
from fastapi import FastAPI

from models import RequestThought, ResponseThought
import actions

app = FastAPI()


# upload a thought
@app.post("/add-thought")
def add_thought(thought: RequestThought):
    actions.add_thought(thought)

    return {
        'created': True,
        'thought': thought
    }



# get thoughts
@app.get("/get-thoughts", response_model=List[ResponseThought])
def get_thoughts():
    thoughts = actions.get_thoughts()
    return thoughts
