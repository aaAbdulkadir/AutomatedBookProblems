#! this finds the first five links of ebay search done through the command line and opens the webpages

from bs4 import BeautifulSoup
import webbrowser, requests, sys

# command line input sys.argv - takes the key word and opens up the first 5 links
if len(sys.argv) != 2:
    print("Invalid usage, must be: python3 test.py 'ebay search'")
    sys.exit()
else:
    # set the command line argument input as the google search you want
    ebaySearch = sys.argv[1]

    # request
    webPage = requests.get(f'https://www.ebay.co.uk/sch/{ebaySearch}').text
    soup = BeautifulSoup(webPage, 'lxml')

    # finds the classes with the links
    links = soup.find_all('a', class_='s-item__link')

    # get first 5 links on ebay search
    for link in links[1:6]:
        if 'href' in link.attrs:
            webbrowser.open(link.attrs['href'])