"""Using FastAPI to Build Python Web APIs."""

# The First API, Step by Step.

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to my web API :)"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


# Data handling with pydantic.
# Receive path parameters and a request body.

# To declare a request body, you use pydantic models,
# with all their power and benefits.


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return {"item_id": item_id, **item_dict}


@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        **item.model_dump(),
    }
