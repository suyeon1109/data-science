from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb+srv://root:root@cluster0.tenpf2n.mongodb.net/?retryWrites=true&w=majority")
    app.database = app.mongodb_client["Cluster0"]
    print("Connected to the MongoDB database!")
    app.collection = app.database["blog"]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


class BlogEntry(BaseModel):
    title: str
    content: str

@app.post("/submit")
async def submit(entry: BlogEntry):
    data = entry.dict()
    result = app.collection.insert_one(data)
    return {"id": str(result.inserted_id)}


@app.put("/update/{id}")
async def update(id: str, entry: BlogEntry):
    data = entry.dict()
    result = app.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"modified_count": result.modified_count}


@app.delete("/delete/{id}")
async def delete(id: str):
    result = app.collection.delete_one({"_id": ObjectId(id)})
    return {"deleted_count": result.deleted_count}


@app.get("/")
async def index():
    entries = app.collection.find()

    view = []
    for entry in entries:
        entry['_id'] = str(entry['_id'])
        view.append(entry)

    return {"entries": view}





















# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.encoders import jsonable_encoder
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# from pydantic import BaseModel

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")


# class BlogEntry(BaseModel):
#     title: str
#     content: str


# @app.on_event("startup")
# def startup_db_client():
#     app.mongodb_client = MongoClient("mongodb+srv://root:root@cluster0.tenpf2n.mongodb.net/?retryWrites=true&w=majority")
#     app.database = app.mongodb_client["Cluster0"]
#     app.collection = app.database["first"]
#     print("Connected to the MongoDB database!")


# @app.on_event("shutdown")
# def shutdown_db_client():
#     app.mongodb_client.close()


# @app.get("/")
# async def index(request: Request):
#     entries = app.collection.find()     # find() = get all data
#     return templates.TemplateResponse("index.html", {"request": request, "entries": entries})


# @app.post("/submit")
# async def submit(request: Request, entry: BlogEntry):
#     data = jsonable_encoder(entry)
#     result = app.collection.insert_one(data)     # document 하나 추가
#     return {"id": str(result.inserted_id)}














# @app.put("/update/{id}")
# async def update(request: Request, id: str, entry: BlogEntry):
#     data = entry.dict()
#     result = app.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
#     return {"modified_count": result.modified_count}


# @app.delete("/delete/{id}")
# async def delete(request: Request, id: str):
#     result = app.collection.delete_one({"_id": ObjectId(id)})
#     # return {"deleted_count": result.deleted_count}
