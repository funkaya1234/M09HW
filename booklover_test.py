# BOOK lover test
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        lover = BookLover("John Doe", "john@example.com", "fiction")
        lover.add_book("The Great Gatsby", 5)
        self.assertIn("The Great Gatsby", lover.book_list['book_name'].values)

    def test_2_add_book(self):
        lover = BookLover("John Doe", "john@example.com", "fiction")
        lover.add_book("1984", 4)
        lover.add_book("1984", 4)
        self.assertEqual(len(lover.book_list[lover.book_list['book_name'] == "1984"]), 1)
                
    def test_3_has_read(self): 
        lover = BookLover("John Doe", "john@example.com", "fiction")
        lover.add_book("To Kill a Mockingbird", 5)
        self.assertTrue(lover.has_read("To Kill a Mockingbird"))
        
    def test_4_has_read(self): 
        lover = BookLover("John Doe", "john@example.com", "fiction")
        self.assertFalse(lover.has_read("The Catcher in the Rye"))
        
    def test_5_num_books_read(self): 
        lover = BookLover("John Doe", "john@example.com", "fiction")
        lover.add_book("The Hobbit", 5)
        lover.add_book("Pride and Prejudice", 4)
        self.assertEqual(lover.num_books_read(), 2)

    def test_6_fav_books(self):
        lover = BookLover("Jane Doe", "jane@example.com", "fiction")
        lover.add_book("The Catcher in the Rye", 2)
        lover.add_book("Brave New World", 4)
        lover.add_book("1984", 5)
        fav_books = lover.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)
