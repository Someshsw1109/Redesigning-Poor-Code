import json  

class Book:  
    def __init__(self, title, author, isbn):  
        self.title = title  
        self.author = author  
        self.isbn = isbn  
        self.available = True  

    def to_dict(self):  
        return {  
            'title': self.title,  
            'author': self.author,  
            'isbn': self.isbn,  
            'available': self.available  
        }  

    @staticmethod  
    def from_dict(data):  
        book = Book(data['title'], data['author'], data['isbn'])  
        book.available = data['available']  
        return book