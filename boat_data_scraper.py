import requests
from bs4 import BeautifulSoup, SoupStrainer
import bs4
import csv

# Instructions
'''
1) Find the URL for each and every
boat being listed on the entire website

2) For each boat, grab and output the following info:
-Boat Maker/Model
-Seller Contact Number
-Price

3) Output the first 800 ads you scraped in a CSV format.
'''

# function to find string between two substrings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# Find number of pages to scrape
start_link = 'http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-55555/Radius-any/Sort-Length:DESC/Page-1,25'
r = requests.get(start_link)
raw_html = r.text
soup = BeautifulSoup(raw_html, 'html.parser')
results = soup.find_all('div', {'class': 'search-viewing'})
text = results[0].text
text2of2 = text.split("of",1)[1]
nText = ''.join(i for i in text2of2 if i.isdigit())
itemsPerPg = 25 # number of listings you want per page
nPages = int(int(nText)/itemsPerPg) + ( int(nText) % itemsPerPg > 0)
print 'pages to scrape: '+`nPages`

# loop to gather all listing links
linkList = []

for page in (range(nPages))[0:2]: ### take out the [0:2] of (range(nPages))[0:2] to do all pages!
    p = page + 1 #since range(nPages) starts at 0
    print 'scraping page '+`p`+' of '+`nPages`+'.'
    link = 'http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-55555/Radius-any/Sort-Length:DESC/Page-'+`p`+','+`itemsPerPg`+''
    
    # build a BeautifulSoup object on the html
    r = requests.get(link)
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')

    # find all individual ad listing links
    search_results = soup.find_all('div', {'class': 'ad-title'})

    print `len(search_results)`+' links on page.'
    
    # add listing links into variable
    for i in range(len(search_results)):
        href = search_results[i].find_all('a')
        url = href[0]['href']
        # turn it from unicode to ascii and add to our list of links
        linkList.append(url.encode('ascii'))
        
    print 'page '+`p`+' of '+`nPages`+' scraped.'

# loop to gather data from each listing

for listing in linkList:
    print `listing`
    link = 'http://www.boattrader.com'+listing
    
    # build a BeautifulSoup object on the html
    r = requests.get(link)
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')

    # find make
    search_make = soup.find_all('span', {'class': 'bd-make'})
    make = search_make[0].text.encode('ascii')

    # find contact
    search_phone = soup.find_all('div', {'class': 'phone'})
    phone = search_phone[0].text.encode('ascii')
    if len(phone) > 0:
        if phone[-1] == ')':
            phone = phone[::-1]
    phone = ''.join(i for i in phone if i.isdigit()) # only keep numbers

    # find price
    search_price = soup.find_all('div', {'id': 'ad-detail-template'})
    price = find_between(search_price[0].text,'price=','"').encode('ascii')
    price = ''.join(i for i in price if i.isdigit()) # only keep numbers

    # add data to csv file
    with open('data.csv','ab') as fp:
        a = csv.writer(fp, delimiter=',')
        data = [[make, phone, price]]
        a.writerows(data)
        fp.close()

print 'Done!'



