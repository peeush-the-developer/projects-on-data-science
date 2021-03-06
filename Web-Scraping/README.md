# Web scraping projects

## What is web scraping?

Web scraping is the process to extract relevant information from the web page on the internet.  
We need this to collect unstructured data present over internet and store the same in some structured way.

## Python libraries to web scrape

### BeautifulSoup

```shell
# Install the library using PIP command
$ pip install bs4
```

```python
# Import library using following line
from bs4 import BeautifulSoup
```

Then we use this library to create BeautifulSoup object that can be used further to extract relevant information from the web page.

## Projects

### 1. Extract historical events in last 100 years

Steps that we followed to extract the information in tabular structure:

- Open the link to the [web page](https://emlii.com/78-events-across-100-years-that-completely-changed-the-world/) in any browser
- Check the HTML structure of similar (and recurring) elements
  _Note: To extract the information from the web page, the information has to follow some structure so that we can extract the information using a script_
- Import `BeautifulSoup` library in your python script
- Create an object for the web page above
- Extract required information for all similar elements those contain required information
- Populate the `pandas` DataFrame with the information
- Process Data cleaning steps if required.

### 2. Extract Trump's lies from the article

Steps that we followed to extract the information in our pandas dataframe:

- Open this [article link](https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html) in any browser
- Check the HTML structure of items that we want to extract.  
  _Note: Use browser's Developer tools (Press F-12 key to activate)_
  ![Browser Developer tools snapshot](02-Trump-Lies-Data/Browser_DevTools_Snapshot.png)
- Import `BeautifulSoup` library in your python project
- Create a Soup object for the web page above
- Extract required information for all lies
- Populate the pandas dataframe with the information
- Process Data cleaning if necessary.
