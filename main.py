from services.auth_service import register_user
success,message = register_user(
    name = "Anitha",
    email= "anithatummala.com",
    password="1234"
)

print(success,message)