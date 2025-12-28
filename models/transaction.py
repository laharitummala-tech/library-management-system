class Transaction:
    def __init__(self,transaction_id,user_id,book_id,issue_date,due_date,return_date,status,fine_amount,fine_paid):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.book_id = book_id
        self.issue_date= issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status
        self.fine_amount = fine_amount
        self.fine_paid = fine_paid
        
        
    def to_dict(self):
        return {
            "transaction_id" : self.transaction_id,
            "user_id" : self.user_id,
            "book_id" : self.book_id,
            "issue_date" : self.issue_date,
            "due_date" :self.due_date,
            "return_date" :self.return_date,
            "status" : self.status,
            "fine_amount" :self.fine_amount,
            "fine_paid" : self.fine_paid      
        }