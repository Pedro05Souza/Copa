from user import User

class UserList:
    users = [] 

    @classmethod
    def add_user(cls, user) -> bool:
        if any(user.username == u.username for u in cls.users):
            return False
        cls.users.append(user)

    @classmethod
    def get_userbyUsername(cls, username) -> User:
        for user in cls.users:
            if user.username == username:
                return user
        return None
    
    @classmethod
    def update_user(cls, user, skill) -> bool:
        for user in cls.users:
            if user.username == user.username:
                user.skill = skill
                return True
        return False
    
    @classmethod
    def delete_user(cls, user) -> bool:
        for userL in cls.users:
            if user.username == userL.username:
                cls.users.remove(userL)
                return True
        return False
    
    
    @classmethod
    def bubble_sort(cls, arr) -> list:
        list_size = len(arr)
        for i in range(list_size):
            for j in range(0, list_size-i-1):
                if arr[j].skill > arr[j+1].skill:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
            
    