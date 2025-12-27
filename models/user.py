class User:
    def __init__(self,user_id,name,email,password,role="user"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        
    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "name" : self.name,
            "email" : self.email,
            "password" : self.password,
            "role" : self.role
        }