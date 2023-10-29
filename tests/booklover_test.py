import unittest
from bklover.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Anna Karenina", 5)
        self.assertEqual(test_object.book_list.book_name[0], "Anna Karenina")
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Anna Karenina", 5)
        test_object.add_book("Anna Karenina", 5)
        self.assertEqual(test_object.num_books, 1)  
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Anna Karenina", 5)
        self.assertEqual(test_object.has_read("Anna Karenina"), True)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Anna Karenina", 5)
        self.assertFalse(test_object.has_read("1984"), "Test 4 has failed")
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Anna Karenina", 5)
        test_object.add_book("1984", 5)
        test_object.add_book("Divergent", 1)
        self.assertEqual(test_object.num_books, 3)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Anna Karenina", 5)
        test_object.add_book("1984", 4)
        test_object.add_book("Divergent", 1)
        test_object.add_book("Pride and Prejudice", 3)
        test_object.add_book("Litte Women", 2)
        for rating in test_object.fav_books().book_rating.values:
            assert rating > 3, "Test 6 failed!"
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
