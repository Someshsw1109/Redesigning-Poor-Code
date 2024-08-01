import json  
import os

from book import Book
from user import User  

class Storage:  
    def __init__(self, filename):  
        self.filename = filename  
        self.data = self.load()  

    def load(self):  
        if os.path.exists(self.filename):  
            with open(self.filename, 'r') as file:  
                return json.load(file)  
        return {'books': [], 'users': []}  

    def save(self):  
        with open(self.filename, 'w') as file:  
            json.dump(self.data, file)  

    def add_book(self, book):  
        self.data['books'].append(book.to_dict())  
        self.save()  

    def add_user(self, user):  
        self.data['users'].append(user.to_dict())  
        self.save()  

    def get_books(self):  
        return [Book.from_dict(b) for b in self.data['books']]  

    def get_users(self):  
        return [User.from_dict(u) for u in self.data['users']]