from utils.file_handler import load_user,save_json
from models.transaction import Transaction
from datetime import date,datetime,timedelta
BOOKS_PATH = "data/books.json"
USERS_PATH = "data/users.json"
TRANSACTION_PATH = "data/transactions.json"
MAX_BORROW_LIMIT = 3
BORROW_DAYS = 14
FINE_PER_DAY = 2

def issue_book(user,book_id):
    transactions_data = load_user(TRANSACTION_PATH)
    transactions = transactions_data.get("transactions",[])
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    
    active_borrows = [
        t for t in transactions
        if t["user_id"] == user["user_id"] and t["status"] == "ISSUED"
    ]
   
    # limit check
    if len(active_borrows) >= MAX_BORROW_LIMIT:
        print("Borrow limit reached, you can borrow only 3 books.")
        return
    
    # check if same book already borrowed
    for t in active_borrows:
        if t["book_id"] == book_id:
            print("You already borrowed this book")
            return
    
    # find book
    for book in books:
        if book["book_id"] == book_id:
            if book["available_copies"] <= 0:
                print('Book not available right now')
                return
            
            book["available_copies"] -= 1
            book["borrow_count"] += 1

            new_id = transactions[-1]["transaction_id"] + 1 if transactions else 1
            # TRANSACTION
            transactions.append(
                Transaction(
                    transaction_id=new_id,
                    user_id=user["user_id"],
                    book_id=book_id,
                    issue_date=str(date.today()),
                    due_date= str(date.today() + timedelta(days=BORROW_DAYS)),
                    return_date=None,
                    status="ISSUED",
                    fine_amount=0,
                    fine_paid=False
                ).to_dict()    
            )
            
            save_json(TRANSACTION_PATH,transactions_data)
            save_json(BOOKS_PATH,books_data)
            
            print(f"Book '{book['title']}' borrowed successfully.")
            return

    print("Book ID not found.")
    
#-------------------------------------------------------------------------------------------------------------------------------#
def view_borrowed_books(user):
    # transactions_data = load_user(TRANSACTION_PATH)
    transactions = load_user(TRANSACTION_PATH).get("transactions",[])
    # books_data = load_user(BOOKS_PATH)
    books = load_user(BOOKS_PATH).get("books",[])
    
    active = [
        t for t in transactions
        if t["user_id"] == user["user_id"] and t["status"] == "ISSUED"
    ]
    if not active:
        print("No books borrowed.")
        return
    
    print("\n ---Your Borrowed books---")
    for t in active:
        for book in books:
            if book["book_id"] == t["book_id"]:
                print(f"ID: {book['book_id']} | {book['title']} by {book['author']} | Due : {t['due_date']}")

#-------------------------------------------------------------------------------------------------------------------------------#

def view_borrow_history():
    users_data = load_user(USERS_PATH)
    users = users_data.get("users",[])
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    transactions = load_user(TRANSACTION_PATH).get("transactions",[])
    if not transactions:
        print("No Transactions found ")
        return

    print("\n---Borrow History---")
    # found = False
    for t in transactions:
        user = next(u for u in users if u["user_id"] == t["user_id"])
        book = next(b for b in books if b["book_id"] == t["book_id"])
        
        print(
            f"{user['name']} | {book['title']} |"
            f"Issued: {t["issue_date"]} |"
            f"Returned: {t["return_date"]} |"
            f"Status: {t["status"]}"
        )
    
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
        for record in user.get("borrowed_books",[]):
            if record["book_id"] == book_id:
                print("Cannot delete book, It is currently borrowed.")
                return
        
        
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            save_json(BOOKS_PATH,books_data)
            print("Book deleted successfully")
            return
        
    print("Book ID not found")
    
#-------------------------------------------------------------------------------------
def return_book(user,book_id):
    books_data = load_user(BOOKS_PATH)
    books = books_data.get("books",[])
    transaction_data = load_user(TRANSACTION_PATH)
    transactions = transaction_data.get("transactions",[])
    today = date.today()
    for t in transactions:
        if (
            t["user_id"] == user["user_id"]
            and t["book_id"] == book_id
            and t["status"] == "ISSUED"
        ):
            due_date = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
            overdue_days = (today - due_date).days
            fine = overdue_days * FINE_PER_DAY if overdue_days > 0 else 0
            
            t["return_date"] = str(today)
            t["status"] = "RETURNED"
            t["fine_amount"] = fine
            t["fine_paid"] = fine == 0
            
            for book in books:
                if book["book_id"] == book_id:
                    book["available_copies"] += 1
                    break
            
            save_json(BOOKS_PATH, books_data)
            save_json(TRANSACTION_PATH, transaction_data)

            print(f"Book returned successfully. Fine: ₹{fine}")
            return

print("This book was borrowed by you.")

#------------------------------------------------------------------------------------------------------------------------------
# def calculate_fine()