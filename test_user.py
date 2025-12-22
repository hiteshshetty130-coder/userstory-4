import unittest
from user import scrap_books
import os

#FILE TO CHECK IF CONTENT EXISTS AND CHECK OTHER THINGS
file="books_data.csv"

class TestCsvFileDownload(unittest.TestCase):
    #Test case 1: Verify Csv file download
    def test_main1(self):
        #check if the file path is not empty and also check if the file path exits
        self.assertIsNotNone(file)
        self.assertTrue(os.path.exists(file))

    #Test Case 2:validate csv file extraction
    def test_main2(self):
        #check if it is correct csv filer and check if it has some data in it
        self.assertTrue(file.endswith(".csv"))
        self.assertGreater(os.path.getsize(file),0)

    #Test Case 3:verify file type and format
    def test_main3(self):
        #check the file type in the system
        self.assertTrue(os.path.exists(file))

    #Test Case 4:validate Data Structure
    def test_main4(self):
        data=scrap_books() #get the value returned from the function
        books_data=data[0]
        #check the data structure is list or not
        self.assertIsInstance(data,list)

        #loop over each data in the list and check if the data as all the required columns
        
        self.assertIn("title",books_data)
        self.assertIn("price",books_data)
        self.assertIn("rating",books_data)
        self.assertIn("availability",books_data)
        self.assertIn("product URL",books_data)

    #Test case 4:Handle missing and invalid data
    def test_main5(self):
        books_data=scrap_books() #get the value returned from the function
        #loops over each data in the list and checks if any value in the dictionary is not none
        for book in books_data:
            for values in book.values():
                self.assertIsNotNone(values)

if __name__=="__main__":
    unittest.main()

