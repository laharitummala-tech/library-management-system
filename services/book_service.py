from utils.file_handler import load_user,save_json
from models.books import Book

BOOKS_FILE = "data/books.json"

def add_new_book(title,author,publisher,published_year,total_copies):
    data = load_user(BOOKS_FILE)
    books = data.get("books",[])
    
    for book in books:
        if book["title"].lower() == title.lower() and book["publisher"].lower() == publisher.lower():
            # book exists --> just add copies
            book["total_copies"] += total_copies
            book["available_copies"] += total_copies
            save_json(BOOKS_FILE,data)
            print(f"Added {total_copies} copies to existing book '{title}'")
            return
    new_book_id = books[-1]["book_id"] + 1 if books else 1
    
    new_book = Book(
        book_id= new_book_id,
        title=title,
        author=author,
        publisher=publisher,
        published_year=published_year,
        total_copies=total_copies,
        available_copies=total_copies,
        borrow_count=0
        
    )
    books.append(new_book.to_dict())
    data["books"] = books
    save_json(BOOKS_FILE,data)
    print(f"New book '{title}' added successfully with ID {new_book_id}!")
    

