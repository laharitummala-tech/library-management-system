class User:
    def __init__(self,user_id,name,email,password,role="user",borrowed_books=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        
    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "name" : self.name,
            "email" : self.email,
            "password" : self.password,
            "role" : self.role,
            "borrowed_books" : self.borrowed_books
        }