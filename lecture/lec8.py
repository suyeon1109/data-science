from fastapi import FastAPI
from pymongo import MongoClient

myproject = FastAPI()

@myproject.on_event("startup")
def startup_db_client():
    myproject.mongodb_client = MongoClient("mongodb+srv://kk1109kk1109:sYFQfX5J28YD71Ls@cluster0.5pusjkc.mongodb.net/?retryWrites=true&w=majority")
    myproject.database = myproject.mongodb_client["Cluster0"]
    print("Connected to the MongoDB database!")

inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "Regular"
    },
    2: {
        "name": "Sprite",
        "price": "1.99",
        "brand": "Regular"
    }
}

"""
get = read
post = create
put = update = write
delete

path parameter
query parameter
request body (database)
"""

@myproject.get("/index")
async def index():
    return {"message":"Welcome to FastAPI world!"}

@myproject.get("/list")
async def index():
    return {"Today is Welcome to FastAPI world!"}

# path parameter
@myproject.get("/list/{item_id}")
async def get_item(item_id:int):
    return inventory[item_id]
"""
@myproject.get("/list/1")
async def get_first_item():
    return inventory[1]
@myproject.get("/list/2")
async def get_first_item():
    return inventory[2]
"""

@myproject.get("/list/{item_id}/name")
async def get_item(item_id:int):
    return inventory[item_id]["name"]

# query parameter
# /list/?item_id=1&user_id=5
@myproject.get("/list/")
async def get_item(item_id:int, user_id: int):
    return inventory[item_id], user_id

# path parameter+query parameter
# 다음 시간에 syntax 까지

