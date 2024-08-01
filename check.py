class Library:  
    def __init__(self, storage):  
        self.storage = storage  

    def checkout_book(self, isbn):  
        for book in self.storage.get_books():  
            if book.isbn == isbn and book.available:  
                book.available = False  
                self.storage.save()  
                return f'Checked out: {book.title}'  
        return 'Book not available'  

    def checkin_book(self, isbn):  
        for book in self.storage.get_books():  
            if book.isbn == isbn and not book.available:  
                book.available = True  
                self.storage.save()  
                return f'Checked in: {book.title}'  
        return 'Book not found'