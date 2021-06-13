# Usage
# python book_price_scraper.py -p 10

import pandas as pd
import requests
from bs4 import BeautifulSoup
import argparse


def get_book_properties(article):
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


def fetch_books_from_url(url):
    response = requests.get(url)
    # print(response)
    # print(response.text[:30])
    soup_obj = BeautifulSoup(response.text, "html.parser")
    # Find elements for article class='product_pod'

    articles = soup_obj.find_all("article", {"class": "product_pod"})
    # print(type(articles))

    results = []
    for article in articles:
        a = get_book_properties(article)
        # print(a)
        results.append(a)

    return results


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
    page_num_placeholder = "[[PAGE_NUM]]"
    url_template = base_url + f"page-{page_num_placeholder}.html"

    books = []
    for page_num in range(args["pages"]):
        url = url_template.replace(page_num_placeholder, str(page_num + 1))
        # print(url)
        books.extend(fetch_books_from_url(url))
        print(f'Progress: {page_num+1}/{args["pages"]}')

    df = pd.DataFrame(
        books, columns=["Title", "Price", "Rating", "Availability", "Url"]
    )

    print(df.shape)
    print(df.head())
    print(df.loc[:5, "Url"])

    df.to_csv("book_prices.csv", index=False)

    print("Completed!")

