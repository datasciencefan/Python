import requests
from bs4 import BeautifulSoup, SoupStrainer
import bs4

# get starting link manually
start_link = 'http://sfbay.craigslist.org/search/sss?sort=rel&query=macbook'

# build a BeautifulSoup object on the html
r = requests.get(start_link)
raw_html = r.text
soup = BeautifulSoup(raw_html, 'html.parser')

# find all individual ad listing links
search_results = soup.find_all('a', {'class': 'i'})

# loop to visit all ad listing links
for item in search_results:
    # create a beautifulsoup object
    link = 'http://sfbay.craigslist.org'+item['href']
    r = requests.get(link)
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')

    # find the price of the item
    price = soup.find_all('span', {'class': 'price'})
    print price[0].text































