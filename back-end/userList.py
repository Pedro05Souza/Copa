from user import User

class UserList:
    users = []
    group1 = [] 
    group2 = [] 

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
    def divide_groups(cls) -> bool:
        if len(cls.users) < 4:
            return False
        sorted_users = sorted(cls.users, key=lambda user: user.skill)
        for i, user in enumerate(sorted_users):
            if i % 2 == 0:
                cls.group1.append(user)
            else:
                cls.group2.append(user)
        return len(cls.group1) == len(cls.group2)





            
    