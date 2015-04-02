def get_soup_for_url(url):
    # Returns the BeautifulSoup object for the given url.
    r = requests.get(url)
    raw_html = r.text
    soup = bs4.BeautifulSoup(raw_html)
    return soup

def get_title(url):
    # Returns the text within the <title> tag for the given url.
    # Return an empty string if it doesn't exists.
    r = requests.get(url)
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    search_results = soup.find_all('title')
    return search_results[0].text

def get_img_count(url):
    # Returns the number of <image> tags present on the page
    # Returns 0 if none exists.
    r = requests.get(url)
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    search_results = soup.find_all('img')
    return len(search_results)

def get_pledge_count():
    # Returns the number of people who have made the pledge on: https://www.teamleada.com/data-year
    # Be sure to parse any relevant text, and return the integer via casting (and NOT string)
    r = requests.get(url)
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    search_results = soup.find_all('strong',{'class':'large-count'})
    number = ''.join(i for i in search_results[0].text if i.isdigit())
    return int(number)
    









