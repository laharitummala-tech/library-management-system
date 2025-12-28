from services.auth_service import register_user,login_user

def register_flow():
    print("\n--- Register ---")
    name = input("Enter name: ")
    email = input("Enter email: ")

    while True:
        password = input("Enter password: ")
        success, message = register_user(name, email, password)

        if success:
            print(message)
            
            # AUTO LOGIN after registration
            success, user = login_user(email,password)
            if success:
                return user
        else:
            print(message)

            # if email exists → go to login
            if message == "Email already exists":
                print("Redirecting to login...")
                return login_flow()
               
            # else keep asking password
            print("Please try again.\n")


def login_flow():
    print("\n--- Login ---")
    email = input("Enter email: ")

    MAX_ATTEMPTS = 3
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        password = input("Enter password: ")
        success, result = login_user(email, password)

        if success:
            print("Login successful")
            print("Welcome,", result["name"])
            return result
        else:
            if result == "Email not found":
                print("Email not registered. Please register.")
                return register_flow()
                

            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(result)

            if remaining > 0:
                print(f"Attempts left: {remaining}")
            else:
                print("Too many attempts. Account locked.")

    
