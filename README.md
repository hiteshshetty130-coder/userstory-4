User-Story Overview
The user-story is to scrap the books details from the scraping website https://books.scrape.com/. To analyze book trends , pricing availability etc.
We have to scarp all the books from the first page and collect all the data scraped and store the data extracted in csv file.

User-story Requirement
•	Scrape all the books from the first page that is index.html
•	And then extract the books from all other pages until the next page exists
•	Extract the required details from the url:
1.	Title
2.	Price
3.	Rating
4.	Availability
5.	Product Url
•	Skip the books if any records is invalid or missing
•	Logging the error if any exception occur 
•	Write the extracted data in the csv file
•	Test the test cases using unit test module

Technology used
Programming language: Python
Library used:
•	Requests library – for the url scrapping
•	Beautiful-soups – For html extraction
•	Csv- for data writing
•	Logging-logging the data
•	Lxml-used for parser
•	Unittest-testing the cases

Website structure
The website link consists of 
•	A homepage which includes front page of 20 books 
•	Includes title price availability rating and other details
•	Contain next page link which includes next 20 books details (pagination)
•	Each book is placed inside article tag of class .product_pod

Data extraction steps
1.	Specify the url of the website you want to scrap
2.	Specify the starting page link
3.	Open the csv file and type the header of the data to scrap
4.	Initialize the empty list 
5.	Create a dictionary of key value pair which is required for getting the rating (as it is given in class)
6.	Create a loop until the next page link exists
7.	Extract the details using HTTP requests by getting the text of current page
8.	Handle 404 and 503 error gracefully (for server busy and if any book is missing)
9.	Extract the data content using the Beautiful Soup Library using lxml parse
10.	Use try except to handle if any the books details is missing or invalid
11.	Run a loop through all the books in the one page continue same for next page
soup.select(article.product_pod)
12.	Extract all the data required by looking into the tag of the page (eg: price=books.select_one(“p.price”).text
13.	For rating data get the class of the tag used for rating and get the value in numbers according to the dictionary key of the rating class
14.	Append all the data extracted to the list 
15.	Write the extracted content in the csv file
16.	Pagination handle :
•	Get the link of the next page if exists 
•	Check if the next page link starts with the catalogue/ else add that to get the current page
17.	Then return the list  



Data structure used
All the data are appending to the list
Data are appended using dictionary ie, key value pairs
Example:
[{“title”: ”light House”,
“price” : “$50”,
“rating” : 3,
“Availability”: “Instock”,
“product Url”: https://books.com/
},
……
]

CSV File writing
The data scraped from the url are written in the csv file using csv module writerow function
Csv file columns are:
1.	Tittle
2.	Price
3.	Availability
4.	Rating
5.	Product url
All the data scraped are written in the csv in their respective columns



Unittest test cases
The test cases are checked using the assert functions of unittest
Test Case 1:Verify csv file download 
•	checked if the csv file which stored all the data exists in the operating system
•	checked if the csv file is not None

Test case 2: Verify csv file extraction
•	checked if it correct csv file or not 
•	check the size of the file wheather it is greater than one or not
Test case 3: validate file type and format
•	Again checked if the correct csv file exists in the system 

Test case 4:validate data structure
•	Got the value returned from the function scrap_books()
•	Check the data structure if the data returned is stored in list are not
•	Loop over all the data  in the list
•	Check if all the columns required or specified exists in the list 
Test case 5:handle missing and invalid data
•	Same way got the value from the function
•	Loop over all the data 
•	For each data which are stored in the form of dict checked if any None value or invalid data exists
Challenges Faced
1.	Pagination Handle – In pagination ie while scraping data from next pages there was some page whose link was not correct like some did not started with “catalogue/” 
So I had to add that if front of the link 
Eg : “catalogue/”+href
2.	Rating data problem – rating are stored in classes according to the classes name are rating icons are displayed, so I had to get the rating in numbers for which I created a dictionary with class name as key and value in integers according to class name 
Then according to the class name I got the value of that key and assigned it as a rating
Eg:”one”:1
3.	Uniitest tesing time – the testing of all five cases takes much time as it tests all the dictionaries insisde the list to check the data structure and also if any column is having invalid data

Final output
Books Scraped = ~1000 books
Output File = “books_data.csv”

Conclusion
The user story is successfully done scrapping the data from the webpage it gracefully handles pagination,error handlings,stores the data in the correct data structure (list),extracts all the required data fields and stored them in csv file and also test cases are successful using unittest.
So now it is possible to analyze book trends, pricing, and stock availability.
























 

