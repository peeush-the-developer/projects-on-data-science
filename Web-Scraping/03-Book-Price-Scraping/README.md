# Scrape book prices

There is a site([Books to scrape](http://books.toscrape.com/index.html)) which is made specifically for Web scraping. Beginners can learn and experienced professionals can validate their learnings using this site to scrape data.

I'll use this site to scrape prices for the books. We have following details about the dataset:

- Total books = 1000
- Total pages = 50
- Books per page = 20
- Javascript included = False

We'll use here **Beautiful Soup** library in python to scrape data. We can use **Selenium's web driver** as well, but since there is not dynamic content (including Javascript), we don't need it.

## Steps

1. Import 'requests`, `BeautifulSoup` libraries
   ```python
   import requests
   from bs4 import BeautifulSoup
   ```
1. Fetch Html response from the site using `requests`
   ```python
   response = requests.get({url})
   ```
1. Load the html content in Soup object
   ```python
   soup_obj = BeautifulSoup(response.text, 'html.parser')
   ```
1. Find all _article_ elements with _class='product_pod'_
1. From each _article_ element, fetch information about Book
   - Title
   - Price
   - Rating
   - Availability
   - Url
1. Prepare a list of information for each book
1. Build a `pandas` DataFrame
1. Save the DataFrame as a CSV file

## Usage

To scrape data from the site, use this shell command:

```shell
$ python book_price_scraper.py -p 50
```
