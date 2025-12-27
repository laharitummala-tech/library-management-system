class Book:
    def __init__(self, book_id,title,author,publisher,published_year,total_copies,available_copies,borrow_count):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.published_year = published_year
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.borrow_count = borrow_count
        
    def to_dict(self):
        return {
            "book_id" : self.book_id,
            "title" : self.title,
            "author" : self.author,
            "publisher" : self.publisher,
            "published_year" :self.published_year,
            "total_copies" : self.total_copies,
            "available_copies" :self.available_copies,
            "borrow_count" :self.borrow_count
            
        }