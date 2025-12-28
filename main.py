# from services.book_service import add_new_book

# add_new_book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925, 3)
# add_new_book("Python Programming","Guido van Rossum","O'Reilly", 2020,10)
# add_new_book("Python Programming","Guido van Rossum","ME", 2022,10)

from utils.menu import admin_menu,user_menu
from utils.register_login_flow import register_flow,login_flow
def main():
    while True:
        print("\n==== Library System ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")
        user = None
        if choice == "1":
            user = register_flow()
        elif choice == "2":
            user = login_flow()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            continue
        
        if not user:
            continue
        
        if user["role"] == "admin":
            admin_menu()
        else:
            user_menu()


if __name__ == "__main__":
    main()
