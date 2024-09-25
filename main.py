# # from fastapi import FastAPI

# from typing import Union

# app = FastAPI()

# fake_items_db = [
#     {"item_name" : "Foo"},
#     {"item_name" : "Bar"},
#     {
#         "item_name" : "Baz"
#     }
# ]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# @app.get("items/{item_id}")
# async def read_item(item_id: str, q:str|None = None, short: bool = False):
#     item = {"item_id" : item_id}
#     if q:
#         item.update({"q" : q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# @app.get(tem"/users/{user_id}/items/{item_id}")
# async def read_user_name(user_id:int, item_id:str, q: str | None = None, short: bool = False):
#     item = {"Item_id" : item_id,  "Owner_id": user_id}
#     if q:
#         item.update({"q" : q})
#     if not short:
#         item.update(
#             {"description:" "This is an amazing item that has a long description"}
#         )
#     return

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id" : item_id , "needy": needy}
#     return item

# from fastapi import FastAPI
# app = FastAPI()

# @app.get({"/items/item_id"})
# async def read_user_item(
#     item_id:str, needy: str, skip : int = 0, limit:  int | None = None):
#     item = {"item_id" : item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item


from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"Price_with_tax" : price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"Item_id": item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result
