import  requests
from bs4 import BeautifulSoup
from lxml.doctestcompare import strip
import csv
import logging

logging.basicConfig(level=logging.INFO)

#function to scrap the data from the web url
def scrap_books():
    try:
        url = "http://books.toscrape.com/"  # web scrapper url
        # first check the main page
        next_page = "index.html"

        #open the file and write the data scraped in the file
        with open("books_data.csv","w",encoding="utf_8")as file:
            csv_file=csv.writer(file)   #write inside the csv file
            csv_file.writerow(['title','price','rating','availability','product URL']) #specify the heading of the data
            books_data=[] #initialize the empty list to store the data

            #create the dictionary because rating is stored as class
            rating_list={
                "One":1,
                "Two":2,
                "Three":3,
                "Four":4,
                "Five":5
            }

            while next_page: #loop until the next page exists
                page_url=url+next_page  #after extracting all the data from the current page extract from next page
                r=requests.get(page_url)
                response=r.text

                #condition for 404 error
                if r.status_code==404:
                    logging.warning("ERROR! page not found")
                    continue

                #for 503 error
                if r.status_code==503:
                    logging.warning("SORRY! Server Unavaialable")
                    break

                #using beautiful soup to extract the data from the content
                soup=BeautifulSoup(response,"lxml")
                try:
                    for books in soup.select("article.product_pod"):# needs book so loop over the all the article tag catalogue
                        #get title price availability product url and rating
                        title=books.h3.a.text
                        price=books.select_one("p.price_color").text
                        availability=books.select_one("p.instock.availability").get_text(strip=True)
                        product_url=books.h3.a["href"]
                        #rating returns a class not number so I take class
                        rating_class=books.select_one("p.star-rating")["class"] #take all inside p tag
                        rating_extract=[c for c in rating_class if c!="star-rating"][0] #take class name which is not equal to star-rating
                        exact_rating=rating_list[rating_extract]  #get the value from the dict according to the class
                        #eg rating_list["three"] = 3

                        #append all the data scraped to the list in the form of dict
                        books_data.append({"title":title,
                                           "price":price,
                                           "rating":exact_rating,
                                           "availability":availability,
                                           "product URL":product_url})

                        #write the content in the csv file
                        csv_file.writerow([title,price,exact_rating,availability,product_url])

                except Exception as e:
                    logging.error("Data is missing Skipping book")
                    continue

                #pagination: extract the books from all the 50pages
                next_link=soup.select_one("li.next a") #check the next page link
                if next_link: #if next page exists then continue
                    href=next_link["href"] #get href of that
                    next_page=(href if href.startswith("catalogue/") else "catalogue/"+href)
                    #check if the href starts with catalogue if not add catalogue and href
                else:
                    return books_data #if next page not exists then return data

    #if any exception occur handle gracefully and if any of books data is empty then handle gracefully
    except Exception as e:
        logging.error(f"Unexcepted error - {e}")

    #return the data for testing
    return books_data,"books_data.csv"

#main function to log the books data which are scraped
def main():
    books=scrap_books()
    logging.info(books) #log the data

if __name__=="__main__":
    main()