class Book:
    def __init__(self,title,author,is_available):
        self.title = title
        self.author = author
        self.is_available = is_available
    
    def book_borrow(self):
        if(self.is_available):
            self.is_available = False
            print("The book is borrowed & now it's unavailable")
        else:
            print("The book is already out")
        
book = Book("The Gem","mariam",True)
book.book_borrow()
book.book_borrow()