from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from user import User
from userList import UserList

app = FastAPI()

origins = [

    # falta fazer
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/user/store/")
async def store_user(user: User):
    if not UserList.get_userbyUsername(user.username):
        UserList.add_user(user)
        return {"message": "User added successfully"}
    else:
        return {"message": "User already exists"}

@app.get("/users/")
async def showUsers():
    if UserList.users:
        return UserList.users
    else:
        return {"message": "No users found"}
      
@app.post("/user/update/")
async def update_user(user: User):
    if user in UserList.users:
        UserList.update_user(user, user.skill)
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=400, detail="User not found")
    
@app.post("/user/delete")  
async def delete_user(user: User):
    if user in UserList.users:
        UserList.delete_user(user)
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=400, detail="User not found")

@app.get("/user/{username}")
async def show_user(username: str):
    user = UserList.get_userbyUsername(username)
    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="User not found")