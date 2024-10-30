# from typing import List, Union

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: Union[str, None] = None
#     description: Union[str, None] = None
#     price: Union[float, None] = None
#     tax = float = 10.5
#     tags: List[str] = []


# items = {
#     "foo":{"name": "Foo", "price": 50.2},
#     "bar": {"name":"bar", "description":"The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
# }

# @app.get("/items/{item_id}", response_model= Item)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.put("/items/{item_id}", response_model= Item)
# async def update_item(item_id: str, item: Item):
#     stored_item_data = items[item_id]
#     stored_item_model = Item(**stored_item_data)
#     update_data = item.dict(exclude_unset= True)
#     updated_item = stored_item_model.copy(update= update_data)
#     items[id] = jsonable_encoder(updated_item)
#     return updated_item

# Classes as Dependencies

from typing import Union

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

fake_items_db = [
    {
        "itme_name": "Foo"
    }, 
    {
        "item_name": "Bar"
    },
    {"item_name": "Baz"}
]

class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response