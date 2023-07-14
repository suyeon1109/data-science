from fastapi import FastAPI, Path
from pymongo import MongoClient
from pydantic import BaseModel

myproject = FastAPI()


@myproject.on_event("startup")
def startup_db_client():
    myproject.mongodb_client = MongoClient(
        "mongodb+srv://root:root@cluster0.tenpf2n.mongodb.net/?retryWrites=true&w=majority")
    myproject.database = myproject.mongodb_client["Cluster0"]
    # myproject.collection = myproject.database["first"]
    print("Connected to the MongoDB database!")


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"},
    2: {
        "name": "Sprite",
        "price": 1.99,
        "brand": "Regular"}
}




class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# @myproject.post("/list/")
# async def create_item(item: Item):
#     return {"message": "You are tricked!"}

@myproject.post("/lists/")
async def create_item(item: Item):
    data = item.dict()
    myproject.database.students.insert_one(data)
    return {"message": "The data is stored successfully!"}



@myproject.get("/")
async def index():
    return {"message": "Hello today is very hot!"}


@myproject.get("/list")
async def today():
    return inventory

@myproject.get("/list/{item_name}")
async def get_item(item_name: str):
    data = myproject.database.students.find_one({"name": item_name})
    data["_id"] = str(data["_id"])
    return data

# #Path parameter
# @myproject.get("/list/{item_id}")
# async def get_item(item_id: int):
#     return inventory[item_id]

#Query parameter
# @myproject.get("/list/")
# async def get_item(num1: int, num2: int):
#     return num1 + num2

# @myproject.get("/list/")
# async def get_item(num1: int = 20, num2: int = 10):
#     return num1 + num2

# @myproject.get("/list/{item_id}")
# async def get_item(item_id: int, num1: int = None):
#     if num1:
#         return {"item_id": item_id, "num1": num1}
#     else:
#         return {"item_id": item_id}

# @myproject.get("/list/{item_id}")
# async def get_item(item_id: int = Path(None, description="WoWOWOOWOW")):
#     return inventory[item_id]

# # gt, lt, ge, le
# @myproject.get("/list/{item_id}")
# async def get_item(item_id: int = Path(None, description="BlahBlah", le=1)):
#     return inventory[item_id]

