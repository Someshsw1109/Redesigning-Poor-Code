from storage import Storage  
from book import Book  
from user import User  
from check import Library  

def main():  
    storage = Storage('library.json')  
    library = Library(storage)  

    while True:  
        print("1. Add Book")  
        print("2. Add User")  
        print("3. Checkout Book")  
        print("4. Checkin Book")  
        print("5. List Books")  
        print("6. List Users")  
        print("7. Exit")  
        choice = input("Choose an option: ")  

        if choice == '1':  
            title = input("Enter book title: ")  
            author = input("Enter book author: ")  
            isbn = input("Enter book ISBN: ")  
            book = Book(title, author, isbn)  
            storage.add_book(book)  
        elif choice == '2':  
            name = input("Enter user name: ")  
            user_id = input("Enter user ID: ")  
            user = User(name, user_id)  
            storage.add_user(user)  
        elif choice == '3':  
            isbn = input("Enter ISBN to checkout: ")  
            print(library.checkout_book(isbn))  
        elif choice == '4':  
            isbn = input("Enter ISBN to checkin: ")  
            print(library.checkin_book(isbn))  
        elif choice == '5':  
            books = storage.get_books()  
            for book in books:  
                print(f"{book.title} by {book.author} - {'Available' if book.available else 'Checked Out'}")  
        elif choice == '6':  
            users = storage.get_users()  
            for user in users:  
                print(f"{user.name} (ID: {user.user_id})")  
        elif choice == '7':  
            break  
        else:  
            print("Invalid option. Please try again.")  

if __name__ == "__main__":  
    main()