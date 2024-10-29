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


# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"Price_with_tax" : price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"Item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q" : q})
#     return result


# Qurey Parameters and String Validations

# from typing import Union
# from fastapi import FastAPI, Query
# from typing_extensions import Annotated

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q:Annotated[Union[str, None], Query(max_length=50)] = None):
#     results = {"ites": [{"item_id": "Foo"}, {"item_id":"Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Request Body

# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         priceWithTax = item.price + item.tax
#         item_dict.update ({"Price with tax" : priceWithTax})
#     print(item_dict)
#     return item_dict

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id":item_id, **item.dict()}

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"Item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# Query Parameter and String Validations

# from typing import Union

# from fastapi import FastAPI, Query
# from typing_extensions import Annotated

# app = FastAPI()

# @app.get("/items")
# async def read_items(
#    int, 
    #     Path(title="The ID of the item to get")
    # ],
    # q:Annotated[
    #     Union[str, None],
    #     Query(alias="item-query")
    # ]= None    q: Annotated[
#         Union[str, None],
#         Query(
#             alias= "item-query",
#             title= "Query String",
#             description= "Query string for the items to search in the database",
#             min_length=3,
#             max_length=50,
#             pattern="^fixedquery$",
#             deprecated=True
#         )
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"},{"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results


# #Path Parameters and Numeric Validations
# from fastapi import FastAPI, Path, Query
# from typing_extensions import Annotated

# app =  FastAPI()
# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: Annotated[int, Path(title="The Id of the item to get", ge=0, le=1000)],
#     q: str, 
#     size: Annotated[float, Query(gt=0, lt=10.5)]
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if size:
#         results.update({"size": size})
#     return results

## Qurey patameters with a Pydantic Model

# from typing import List

# from fastapi import FastAPI, Query
# from pydantic import BaseModel, Field
# from typing_extensions import Annotated, Literal

# app = FastAPI()

# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}

#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at",
#     tags: List[str] = []

# @app.get("items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query


## Body - Multiple Parameters
# from typing import Union

# from fastapi import FastAPI, Path, Body
# from pydantic import BaseModel
# from typing_extensions import Annotated

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int, 
#     item: Item,
#     user: User, 
#     importance: Annotated[int, Body()],
#     q: Union[str, None] = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


#Body - Fields

# from typing import Union
# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field
# from typing_extensions import Annotated

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = Field(default=None, title="The description of the item", max_length=300)
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: Union[float, None] = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id}
#     return results


#Body - Nested Models

# from typing import List, Set, Union

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()

# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     images: Union[List[Image], None] = None

# class Offer(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     items: List[Item]

# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer

# @app.post("/images/multiple/")
# async def create_multiple_images(images: List[Image]):
#     for image in images:
#         urlid = image.url
#         urlName = image.name
#     return images

## Declare Request Example Data

# from typing import Union
# from fastapi import FastAPI, Body
# from pydantic import BaseModel
# from typing_extensions import Annotated

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#     Item,
#     Body(
#        openapi_examples={
#            "normal":{
#                "summary": "A normal example",
#                "description": "A **normal** item works correctly",
#                "value":{
#                    "name": "Foo",
#                    "description": "A very nice Item",
#                    "price": 35.4,
#                    "tax": 3.2
#                },
#            },
#            "converted":{
#                "summary": "An example with converted Data",
#                "description": "FastAPI can convert price string",
#                "value":{
#                    "name": "Bar",
#                    "price": "35.4",
#                }
#            },
#            "invalid":{
#                "summary": "Invalid data is rejected with an error",
               

#                "value":{
                   
#                    "name": "Baz",
#                    "price": "thirty five point four"
#                }
#            }
#        }
#     )
#     ]
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# Extra Data Types
# from datetime import datetime, time, timedelta
# from typing import Union
# from uuid import UUID

# from fastapi import Body, FastAPI
# from typing_extensions import Annotated

# app = FastAPI()

# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: Annotated[datetime, Body()],
#     end_datetime: Annotated[datetime, Body()],
#     process_after: Annotated[timedelta, Body()],
#     repeat_at: Annotated[Union[time, None], Body()]= None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration
#     }


# "Cookie Parameters
# from typing import Union

# from fastapi import FastAPI, Cookie
# from typing_extensions import Annotated

# app = FastAPI()

# @app.get("/items")
# async def read_items(ads_id: Annotated[Union[str, None], Cookie()]= None):
#     return {"ads_id": ads_id}


#Header Parameters

# from typing import Union, List

# from fastapi import FastAPI, Header
# from typing_extensions import Annotated

# app = FastAPI()

# @app.get("/items/")
# async def read_iems(
#     x_token: Annotated[
#         Union[List[str], None], Header()
#     ] = None
# ):
#     return {"X-Token Values":x_token}

# Cookie Parameter Model

# from typing import Union

# from fastapi import FastAPI, Cookie
# from pydantic import BaseModel
# from typing_extensions import Annotated

# app = FastAPI()

# class Cookies(BaseModel):
#     session_id: str
#     fatebook_traker: Union[str, None] = None
#     googall_tracker: Union[str, None] = None

# @app.get("/items/")
# async def read_items(cookies: Annotated[Cookies, Cookie()]):
#     return cookies


#Header Parameter Models

# from typing import List, Union

# from fastapi import FastAPI, Header
# from pydantic import BaseModel
# from typing_extensions import Annotated

# app = FastAPI()

# class CommonHeaders(BaseModel):
#     host: str
#     save_data: bool
#     if_modified_since: Union[str, None] = None
#     traceparent: Union[str, None] = None
#     x_tag: List[str] = []

# @app.get("/items/")
# async def read_items(headers: Annotated[CommonHeaders, Header()]):
#     return headers

# Response Model - Return Type

# from typing import List, Union, Any

# from fastapi import FastAPI , Response
# from fastapi.responses import JSONResponse, RedirectResponse
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price":62, "tax": 20.2 },
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
# }

# @app.get("/items/{item_id}", response_model=Item, response_model_include= {'name', 'description','price'})
# async def read_item_name(item_id: str):
#     return items[item_id]

# @app.get("/items/{item_id}/public", response_model= Item, response_model_exclude={'tax'})
# async def read_item_public_data(item_id: str):
#     return items[item_id]

# Multiple Models
# from typing import List

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str


# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/items/", response_model=List[Item])
# async def read_items():
#     return items

# Form Data

# from fastapi import FastAPI , Form
# from pydantic import BaseModel
# from typing_extensions import Annotated

# app = FastAPI()

# class FormData(BaseModel):
#     username: str
#     password: str
#     model_config = {"extra": "forbid"}

# @app.post("/login/")
# async def login(data:Annotated[FormData, Form()]):
#     return data
 

# Request Files
# from typing import Union, List

# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse
# from typing_extensions import Annotated

# app = FastAPI()

# @app.post("/files/")
# async def create_file(files: Annotated[List[bytes], File()]):
#     return {"file_sizes" : [len(file) for file in files] }

# @app.post("/uploadfile/")
# async def create_upload_file(
#     files: List[UploadFile]
# ):
#     return {"filename" : file.filename for file in files}
# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action = "/files/" entype = "multipart/formdata" method = "post">
# <input name = "files" type = "file" multiple>
# <input type = "submit">
# </form>
# <form actioin = "/uploadfiles/" enctype = "multipart/form-data" method = "post">
# <input name = "files" type = "file" multiple>
# <input type = "submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)

# Request Forms and Files

# from fastapi import fastAPI, File, Form, UploadFile
# from typing_extensions import Annotated

# app = fastAPI()

# @app.post('/files')
# async def create_file(
#     file: Annotated[bytes, File()],
#     fileb: Annotated[UploadFile, File()],
#     token: Annotated[str, Form()],
# ):
#     return{
#         "file_size": len(file),
#         "token": token,
#         'file_content_type': fileb.content_type
#     }

# Path Operation Configuration

# from enum import  Enum

from typing import Set, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Tags(Enum):
#     items = "items"
#     users = "users"

# @app.get("/items/", tags= [Tags.items])
# async def get_items():
#     return ["Portal gun", "Plumbus"]

# @app.get("/users/", tags= [Tags.users])
# async def read_user():
#     return ["Rick", "Morty"]

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()

@app.post(
    "/items/",
    response_model= Item,
    summary= "Create an Item",
    response_description= "The created item"
    
)
async def create_item(item: Item):
    """
    Create an item with all the information

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item

    """
    return item

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/", tags= ["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]

# @app.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": 'Johndoe'}]

# @app.get("/elements/", tags= ["items"], deprecated= True)
# async def read_elements():
#     return [ {"item_id": "Foo"}]