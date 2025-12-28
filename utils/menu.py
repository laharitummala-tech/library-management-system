from services.book_service import add_new_book, view_books
from services.transaction_service import issue_book,view_borrowed_books
def get_non_empty_string(prompt):
    value = input(prompt).strip()
    while value == "":
        print("Input cannot be empty.")
        value = input(prompt).strip()  
        # here if the value is empty keep asking the user again
        # until they type something valid
    return value # returns the valid, non-empty string

def get_valid_year(prompt):
    year = input(prompt)
    while not year.isdigit() or int(year) < 1000 or int(year) > 2025:
        print("Enter a valid published year.")
        year = input(prompt)
    return int(year)


# this is to handle if user enters negative number for copies 
def get_positive_integer(prompt):
    value = input(prompt)
    while not value.isdigit() or int(value) <= 0:
        print("Enter a positive number.")
        value = input(prompt)
    return int(value)
                      
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add book")
        print("2. View books")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            
            title = get_non_empty_string("Enter book title")
            author =  get_non_empty_string("Enter author name: ")
            publisher =  get_non_empty_string("Enter publisher name: ")
            published_year = get_valid_year("Enter published year :")
            total_copies = get_positive_integer("Enter total copies: ")
            add_new_book(
                title,
                author,
                publisher,
                published_year,
                total_copies
            )
        elif choice == "2":
            view_books()
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        
    
def user_menu(user):
    while True:
        print("\n --- User Menu ---")
        print("1. View books")
        print("2. Borrow book")
        print("3. View Borrowed books")
        print("4. Logout")
        choice = input("Enter choice :")
        if choice == "1":
            view_books()
        elif choice == "2":
            view_books()
            book_id = input('Enter book ID to borrow: ')
            if book_id.isdigit():
                issue_book(user,int(book_id))
                
            else:
                print("Invalid book ID")
        
        elif choice == "3":
            view_borrowed_books(user)
            
        elif choice == "4":
            print("Logged out")
            break
        else:
            print("Invalid choice")