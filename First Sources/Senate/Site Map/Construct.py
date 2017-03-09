from requests import get
from bs4 import BeautifulSoup

def view_structure(url):
    soup = BeautifulSoup(get(url).content, 'lxml')
    print(soup.prettify())

view_structure('http://www.grassley.senate.gov')

def find_links(url):
    soup = BeautifulSoup(get(url).content, 'lxml')
    body = soup.find('body')

    links = body.find_all('a')

    relative_links = []
    for link in links:
        try:
            if link['href'].startswith('/'):
                relative_links.append(link['href'])

        except:
            pass

    return relative_links

rel_links = find_links('http://www.grassley.senate.gov')





relative_links = []
for link in links:
    try:
        if link['href'].startswith('/'):
            relative_links.append(link['href'])

    except:
        pass
