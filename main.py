from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def available_books():
    i = 0
    for book in library_books:
        availability = library_books[i]["available"]
        if availability == True:
            print("Book ID: " + library_books[i]["id"])
            print("Title: " + library_books[i]["title"])
            print("Author: " + library_books[i]["author"])
            print()
            
        i+=1



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def specific_author_genre():
    user_choice = input("Would you like to read a certain author's book or genre? Enter author or genre: ").lower()
    if user_choice == 'author':
        author = input("Enter author name: ").lower()
        i = 0
        for book in library_books:
            book_author = library_books[i]["author"].lower() #variable which filters through the author's whose books we have
            
            if author == book_author:
                print("Book Title: " + library_books[i]["title"])
                
            i+=1
    elif user_choice == 'genre':
        genre = input("Enter genre: ").lower()
        i = 0
        for book in library_books:
            book_genre = library_books[i]["genre"].lower() #variable which filters through the genre author's books we have
            
            if genre == book_genre:
                print("Book Title: " + library_books[i]["title"])
                
            i+=1

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def book_checkout():
    user_book_id = input("Enter book ID: ")
    book_num = int(user_book_id[1]) - 1
    checkouts = library_books[book_num]["checkouts"]
    availability = library_books[book_num]["available"]
    if availability == True:
        availability = False
        current_date = datetime.today()
        due_date = current_date + timedelta(weeks = 2)
        checkouts+=1
    else:
        print("Sorry, that book has already been checked out.")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def book_return():
    user_book_id = input("Enter book ID: ")
    book_num = int(user_book_id[1]) - 1
    availability = library_books[book_num]["available"]
    if availability == False:
        availability = True
        due_date = library_books[book_num]["due_date"]
        due_date = None


# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue_books():
    current_date = str(datetime.today())
    for book in library_books:
        due_date = book["due_date"]
        if due_date != None:
            if due_date != current_date and book["checkouts"] > 0:
                print(book["title"])
        print()
# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
class Book:
    def __init__(self, available_books, specific_author_genre, book_checkout, book_return):
        self.available_books = available_books()
        self.specific_author_genre() = specific_author_genre()
        self.book_checkout = book_checkout()
        self.book_return = book_return()
        
    def available_books():
        i = 0
        for book in library_books:
            availability = library_books[i]["available"]
            if availability == True:
                print("Book ID: " + library_books[i]["id"])
                print("Title: " + library_books[i]["title"])
                print("Author: " + library_books[i]["author"])
                print()
                
            i+=1
            
    def specific_author_genre():
        user_choice = input("Would you like to read a certain author's book or genre? Enter author or genre: ").lower()
        if user_choice == 'author':
            author = input("Enter author name: ").lower()
            i = 0
            for book in library_books:
                book_author = library_books[i]["author"].lower() #variable which filters through the author's whose books we have
                
                if author == book_author:
                    print("Book Title: " + library_books[i]["title"])
                    
                i+=1
        elif user_choice == 'genre':
            genre = input("Enter genre: ").lower()
            i = 0
            for book in library_books:
                book_genre = library_books[i]["genre"].lower() #variable which filters through the genre author's books we have
                
                if genre == book_genre:
                    print("Book Title: " + library_books[i]["title"])
                    
                i+=1
    
    def book_checkout():
        user_book_id = input("Enter book ID: ")
        book_num = int(user_book_id[1]) - 1
        checkouts = library_books[book_num]["available"]
        availability = library_books[book_num]["available"]
        if availability == True:
            availability = False
            current_date = datetime.today()
            due_date = current_date + timedelta(weeks = 2)
            checkouts+=1
        else:
            print("Sorry, that book has already been checked out.")

    def book_return():
        user_book_id = input("Enter book ID: ")
        book_num = int(user_book_id[1]) - 1
        availability = library_books[book_num]["available"]
        if availability == False:
            availability = True
            due_date = library_books[book_num]["due_date"]
            due_date = None
        
        
print("Welcome to the Library!")
print("How may I help you today? Please choose from an option below.")
print("1. View Available Books")
print("2. Search for specific Authors/Genres")
print("3. Book Checkout")
print("4. Book Return")
print()
user_option = int(input("Enter the number of the option chosen: "))
print()
option_chosen = False
while option_chosen == False:
    if user_option == 1:
        option_chosen = True
        available_books()
    elif user_option == 2:
        option_chosen = True
        specific_author_genre()
    elif user_option == 3:
        option_chosen = True
        book_checkout()
    elif user_option == 4:
        option_chosen = True
        book_return()
    else:
        print("Invalid Response. Please Try Again.")
        user_option = int(input("Enter the number of the option chosen: "))
# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

# if __name__ == "__main__":
#     # You can use this space to test your functions
#     pass