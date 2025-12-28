from utils.file_handler import load_user,save_json
from models.transaction import Transaction
BOOKS_PATH = "data/books.json"
USERS_PATH = "data/users.json"
MAX_BORROW_LIMIT = 3

def issue_book(user,book_id):
    users_data = load_user(USERS_PATH)
    users = users_data.get("users",[])
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    
    # find logged_in user
    for i in users:
        if i["user_id"] == user["user_id"]:
            current_user = i
            break
    else:
        print("user not found")
        return
    borrowed = current_user.get("borrowed_books",[])
   
    # limit check
    if len(borrowed) >= MAX_BORROW_LIMIT:
        print("Borrow limit reached, you can borrow only 3 books.")
        return
    
    # find book
    for book in books:
        if book["book_id"] == book_id:
            if book["available_copies"] <= 0:
                print('Book not available right now')
                return
            
            if book_id in borrowed:
                print("You already borrowed this book")
                return
                
            # TRANSACTION
            book["available_copies"] -= 1
            book["borrow_count"] += 1
            borrowed.append(book_id)
            
            current_user["borrowed_books"] = borrowed
            
            save_json(USERS_PATH,users_data)
            save_json(BOOKS_PATH,books_data)
            
            print(f"Book '{book['title']}' borrowed successfully.")
            return

    print("Book ID not found.")
    
#-------------------------------------------------------------------------------------------------------------------------------#
def view_borrowed_books(user):
    users_data = load_user(USERS_PATH)
    users = users_data.get("users",[])
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    
    for i in users:
        if i["user_id"] == user["user_id"]:
            borrowed_ids = i.get("borrowed_books",[])
            break
        
    else:
        print("User not found")
        return
    
    if not borrowed_ids:
        print("No books borrowed")
        return
    
    print("\n--- Your borrowed books")
    for book in books:
        if book["book_id"] in borrowed_ids:
            print(f"ID: {book['book_id']} | {book['title']} by {book['author']}")

#-------------------------------------------------------------------------------------------------------------------------------#

def view_borrow_history():
    users_data = load_user(USERS_PATH)
    users = users_data.get("users",[])
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    if not users:
        print("No users found ")
        return
    
    print("\n---Borrow History---")
    found = False
    
    for user in users:
        borrowed =users.get("borrowed_books",[])
        if borrowed:
            found = True
            print(f"\n User: {user["name"]} (ID: {user["user_id"]})")
            for book in books:
                if book["book_id"] in borrowed:
                    print(f" -  {book["title"]} by {book["author"]}")
    
    if not found:
        print("No books issued yet")
    
#-------------------------------------------------------------------------------------------------------------------------------#

    
def update_book(book_id):
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    for book in books:
        if book["book_id"] == book_id:
            print("\n----Update Book ---")
            print("Press Enter to skip updating the field")
            
            title = input(f"Title [{book["title"]}]: ").strip()
            author = input(f"Author [{book["author"]}]: ").strip()
            publisher = input(f"Publisher [{book['publisher']}]: ").strip()
            published_year = input(f"Published Year [{book['published_year']}]: ").strip()
            total_copies = input(f"Total Copies [{book['total_copies']}]: ").strip()
            
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if publisher:
                book["publisher"] = publisher
            if published_year.isdigit():
                book["published_year"] = int(published_year)
            if total_copies.isdigit():
                book["total_copies"] = int(total_copies)
                
            save_json(BOOKS_PATH, books_data)
            print("Book updated successfully.")
            return

    print("Book ID not found.")
    
    
#---------------------------------------------------------------------------------------------------------------

def delete_book(book_id):
    users_data = load_user(USERS_PATH)
    users = users_data.get('users',[])
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    
    for user in users:
        if book_id in user.get("borrowed_books",[]):
            print("Cannot delete book, It is currently borrowed.")
            return
        
        
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            save_json(BOOKS_PATH,books_data)
            print("Book deleted successfully")
            return
        
    print("Book ID not found")
    
    
    
    
    
    
# def return_book()



# def calculate_fine()