# test.py
from booklover import booklover

# Test the BookLover class
def test_function():
    # Create an instance of the BookLover class
    test_object = booklover.BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    
    # Test adding a book
    test_object.add_book("War of the Worlds", 4)
    
    # Test if the book is in the list
    result_has_read = test_object.has_read("War of the Worlds")
    print(f"Has read 'War of the Worlds': {result_has_read}")
    
    # Test number of books read
    num_books = test_object.num_books_read()
    print(f"Number of books read: {num_books}")
    
    # Test favorite books (with rating > 3)
    fav_books = test_object.fav_books()
    print(f"Favorite books (rating > 3):\n{fav_books}")

if __name__ == "__main__":
    test_function()

