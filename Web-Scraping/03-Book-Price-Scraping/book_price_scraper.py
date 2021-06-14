# Usage
# python book_price_scraper.py -p 10

from bs4.element import PageElement
import pandas as pd
import requests
from bs4 import BeautifulSoup
import argparse


def extract_book_record(article: PageElement) -> tuple:
    """
    Extract information from a BeautifulSoup's PageElement related to a book item

    Arguments:
        article: PageElement containing individual book information
    
    Returns:
        A tuple containing book information
    """

    # Rating
    p_rating = article.find("p", {"class": "star-rating"})
    rating = p_rating["class"][1]

    # Book title, url
    a_inside_h3 = article.find("h3").find("a")
    book_title = a_inside_h3["title"]
    book_url = base_url + a_inside_h3["href"]

    # Book price
    p_price = article.find("p", {"class": "price_color"})
    price = p_price.text[2:]

    # Availability
    p_instock = article.find("p", {"class": "availability"})
    availability = p_instock.contents[2].strip()

    return book_title, price, rating, availability, book_url


def fetch_books_from_page(url: str) -> list:
    """
    Extract book records from a page provided with the url.

    Arguments:
        url: Url of the page
    
    Returns:
        A list of book records
    """

    response = requests.get(url)
    # print(response)
    # print(response.text[:30])
    soup_obj = BeautifulSoup(response.text, "html.parser")

    # Find elements for article class='product_pod'
    articles = soup_obj.find_all("article", {"class": "product_pod"})
    # print(type(articles))

    for article in articles:
        book_record = extract_book_record(article)
        # print(a)
        yield book_record


if __name__ == "__main__":
    # Read from Command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-p",
        "--pages",
        type=int,
        required=True,
        choices=range(1, 51),
        help="Total pages to scrape",
    )
    args = vars(ap.parse_args())

    # Define URLS
    base_url = "http://books.toscrape.com/catalogue/"
    # Define variable to contain placeholder for page_num to build urls for different pages
    page_num_placeholder = "[[PAGE_NUM]]"
    # Define variable for templating the urls that can accommodate different page numbers
    url_template = base_url + f"page-{page_num_placeholder}.html"

    # Empty list to contain list of tuple for book
    books = []
    for page_num in range(args["pages"]):
        # Replace placeholder with actual page number
        url = url_template.replace(page_num_placeholder, str(page_num + 1))
        # print(url)
        # Append all the tuples for books returned by function in the list
        books.extend(fetch_books_from_page(url))
        print(f'Progress: {page_num+1}/{args["pages"]}')

    # Build a pandas DataFrame from list of books
    df = pd.DataFrame(
        books, columns=["Title", "Price", "Rating", "Availability", "Url"]
    )

    print(df.shape)
    print(df.head())
    # print(df.loc[:5, "Url"])

    # Write the DataFrame to a CSV file.
    df.to_csv("book_prices.csv", index=False)

    print("Completed!")
