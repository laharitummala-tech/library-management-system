from services.book_service import add_new_book

add_new_book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925, 3)
add_new_book("Python Programming","Guido van Rossum","O'Reilly", 2020,10)
add_new_book("Python Programming","Guido van Rossum","ME", 2022,10)

#--------------------------------REGISTER ----------------------------
# from services.auth_service import register_user
# success,message = register_user(
#     name = "Anitha",
#     email= "anithatummala.com",
#     password="1234"
# )

# print(success,message)
#--------------------LOGIN------------------------------------#
# from services.auth_service import login_user
# email = input("Enter email: ")
# success,result = login_user(email,"")

# if result == "Email not found":
#     print("Email not registered. Please register first.")
# else:
#     MAX_ATTEMPTS = 3
#     for i in range(MAX_ATTEMPTS):
#         password = input("Enter password :")
#         success,message=login_user(email,password)
    
#         if success:
#             print("Login success")
#             print(message)
#             break
    
#         else:
#             remaining = MAX_ATTEMPTS - i - 1
#             print(message)
#             if remaining > 0:
#                 print(f"Attempts left : {remaining}")
#             else:
#                 print("Account locked, try again")