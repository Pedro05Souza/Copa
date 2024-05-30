from fastapi import FastAPI
from user import User
from userList import UserList

app = FastAPI()

@app.get("/user/ {username} / {skill} ")
async def get_user(username: str, skill: str):
    return UserList.add_user(User(username, skill))

@app.post("/user/ {username} ")
async def get_user(username: str):
    return UserList.get_userbyUsername(username)