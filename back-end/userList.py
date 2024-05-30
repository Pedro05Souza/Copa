from user import User

class UserList:
    def __init__(self):
        self.users = [] 

    def add_user(self, user) -> bool:
        for user in self.users:
            if user.username == user.username:
                return False
        self.users.append(user)

    def get_userbyUsername(self, username) -> User:
        for user in self.users:
            if user.username == username:
                return user
            
    