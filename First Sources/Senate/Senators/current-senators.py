import requests
from bs4 import BeautifulSoup
import pandas as pd


# Get the websites of senators
# Now stored in Senators and Sites.pkl
def extract_senators_and_websites():
    file = open('/Users/duncangh/PycharmProjects/OnTheRecord/First Sources/Senate/Senators/senate.html', 'r').read()
    soup = BeautifulSoup(file, 'lxml')

    links = soup.find_all('a')

    site_dict = {}
    for link in links[18:216]:
        if link['href'].endswith('.gov') or link['href'].endswith('.gov/'):
            if 'www.' not in link.text.strip():
                site_dict[link.text.strip()] = link['href']

    return site_dict

# extract_senators_and_websites()

def parse_press_releases():
    df = pd.read_excel('Full List.xlsx')