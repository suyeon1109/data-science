from fastapi import FastAPI

myproject = FastAPI()

dict = {
    "1" : "Monday",
    "2" : "Tuesday",
    "3" : "Wednesday",
    "4" : "Thursday"
}

@myproject.get("/index")
async def index():
    return {"message":"Welcome to FastAPI world!"}

@myproject.get("/list")
async def index():
    return {"Today is Welcome to FastAPI world!"}