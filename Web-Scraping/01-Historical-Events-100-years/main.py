# Usage
# python main.py

# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get response for the desired web page request
response = requests.get(
    'https://emlii.com/78-events-across-100-years-that-completely-changed-the-world/')

# Create BeautifulSoup object for the desired web page
soup_obj = BeautifulSoup(response.text, 'html.parser')

# Get Objects of similar type
events = soup_obj.find_all(class_='article-inner-block')

print(f"Total no. of events = {len(events)}")

events_list = []
for obj in events:
    heading = obj.find('h2', class_='article-subtitle')
    title, year = None, None
    if heading:
        title = heading.text[3:-7]
        year = heading.text[-5:-1]
        # print(title, year)
    image = obj.find('img')
    url = None
    if image:
        url = image['src']
        # print(url)
    desc_tag = obj.find('p', class_='article-inner-description')
    desc = None
    if desc_tag:
        desc = desc_tag.text
        # print(desc.text)
    events_list.append((title, year, url, desc))

df = pd.DataFrame(events_list, columns=[
                  'Title', 'Year', 'Img_url', 'Description'])
print(df.shape)
