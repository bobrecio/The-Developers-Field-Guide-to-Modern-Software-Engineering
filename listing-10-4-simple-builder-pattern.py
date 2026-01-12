class UserBuilder: 

    def __init__(self): self.data = {} 

    def name(self, n): self.data["name"] = n; return self 

    def email(self, e): self.data["email"] = e; return self 

    def build(self): return self.data 

 

user = UserBuilder().name("Alice").email("alice@example.com").build() 