 

 

    def get_user_by_id(self, user_id: int) -> UserModel: 

        # This is where the DB query would happen 

        pass 

 

 

# --- Domain Layer --- 

class UserService: 

    def __init__(self, repository: UserRepository): 

        self.repository = repository 

 

    def get_user_name(self, user_id: int) -> str: 

        user = self.repository.get_user_by_id(user_id) 

        if user: 

            return user.name 

        return None 

 

 

# --- Usage Example --- 

repo = UserRepository() 

service = UserService(repo) 

 

name = service.get_user_name(123) 

print(name) 