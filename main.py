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

from fastapi import FastAPI
app = FastAPI()

@app.get({"/items/item_id"})
async def read_user_item(
    item_id:str, needy: str, skip : int = 0, limit:  int | None = None):
    item = {"item_id" : item_id, "needy": needy, "skip": skip, "limit": limit}
    return item