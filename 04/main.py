from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/sum")
def sum(a: int, b: int):
    # if not isinstance(a, int) or not isinstance(b, int):
    #     raise HTTPException(status_code=422, detail="[ERROR] a and b must be int")
    return {"sum": a + b}