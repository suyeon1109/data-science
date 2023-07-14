from fastapi import FastAPI, Path
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId
import certifi

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb+srv://kk1109kk1109:sYFQfX5J28YD71Ls@cluster0.5pusjkc.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    app.database = app.mongodb_client["Cluster0"]
    print("Connected to the MongoDB database!")

# 네이버 지식인 같은 Q&A 보드 웹사이트

# <Model>
# Question: title, content, user_id
# Answer: question_id, content, user_id
# User: user_name, password, age 

# <API>
class User(BaseModel):
    name:str
    password:str
    age:int

@app.post("/user") # 유저 생성하기
def create_user(user:User):
    user_info=user.dict()
    app.database.users.insert_one(user_info)
    
@app.get("/user/{user_id}")	# 유저 정보 가져오기
async def get_user_info(user_id:str):
    user = app.database.users.find_one({"_id":ObjectId(user_id)})
    user["_id"] = str(user["_id"])
    return user

class change(BaseModel):
    name: str
    password: str
    age: int

@app.put("/user/{user_id}")	# 유저 정보 수정하기
async def edit(user_id: str, entry: change):
    data = entry.dict()
    result = app.database.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

@app.delete("/user/{user_id}")	# 유저 정보 삭제하기
async def delete(user_id:str):
    result = app.database.users.delete_one({"_id": ObjectId(user_id)})

@app.post("/questions")	# 질문 생성하기
async def create_question(q:str):
    data = q.dict()
    result = app.database.questions.insert_one(data)
    # return 

# @app.get("/questions")	# 모든 질문 가져오기
# @app.get("/questions/{question_id}") # 특정 질문 1개 가져오기
# # 질문 수정하기
# # 질문 삭제하기

# @app.post("/questions/{question_id}/answers")	# 특정 질문에 대한 답변 생성하기
# # 특정 질문에 대한 모든 답변 가져오기
# # 답변 수정하기
# # 답변 삭제하기