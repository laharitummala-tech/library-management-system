# "auth_service receives an email.
# It checks all users loaded from users.json.
# If any user has the same email, registration fails.
# Otherwise, add a new user object to JSON."

from utils.file_handler import load_user, save_json
from models.user import User
USERS_FILE = "data/users.json"

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_digit = False
    has_upper = False
    has_specialchar = False
    special_chars = "@#$%^&*"
    
    for i in password:
        if i.isdigit():
            has_digit = True
        elif i.isupper():
            has_upper=True
        elif i in special_chars:
            has_specialchar = True
            
    if not has_digit:
        return False, "Password must contain at least one digit"
    if not has_upper:
        return False, "Password must contain at least one capital letter"
    if not has_specialchar:
        return False, "Password must contain at least one special character"
      
    return True, "Valid password"
    
def register_user(name,email,password):
    data = load_user(USERS_FILE)
    users = data.get("users" ,[])
    
    # check if email already exists
    for user in users:
        if user["email"] == email:
            return False, "Email already exists"
        
    # password validation
    is_valid,message=is_valid_password(password)
    if not is_valid:
        return False,message
    
    new_user_id = users[-1]["user_id"] + 1 if users else 1
    
    # create user object
    new_user = User(
        user_id = new_user_id,
        name=name,
        email=email,
        password=password,
        role="user"
    )
    
    users.append(new_user.to_dict()) # convert user-->dict, add to users list
    data["users"] = users # put updated users back
    save_json(USERS_FILE,data) # save into JSON file
    
    return True, "User registered successfully"



def login_user(email,password):
    data = load_user(USERS_FILE)
    users = data.get("users",[])
    
    for user in users:
        if user["email"] == email:
            if user["password"] == password:
                return True, user  # Login succes
            else:
                return False, "Incorrect password"            
    return False, "Email not found"