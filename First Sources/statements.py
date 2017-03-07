# Read all official white house statements
import requests
from bs4 import BeautifulSoup



def scrape_speeches():
    """Scrape all of the speeches available on the White House Page"""
    # Dictionary holding the title of speech/address : content of it
    title_content = {}

    # Todo: Make dyanmic -- so can handle various length pages
    for i in range(7):

        base_url = 'https://www.whitehouse.gov/briefing-room/speeches-and-remarks?term_node_tid_depth=31&page=%s' % str(
            i)

        resp = requests.get(base_url)
        soup = BeautifulSoup(resp.content, 'lxml')

        links = soup.find('div', {'class': 'view-content'}).find_all('a')

        for link in links:
            speech_url = 'https://www.whitehouse.gov%s' % link['href']
            title_content[speech_url] = extract_text(speech_url)

    return title_content

def extract_text(url):
    """Extract all the text content from the url of the speech"""

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')

    content = ''

    p_tags = soup.find_all('p')
    for p_tag in p_tags:
        try:
            if p_tag.text != 'Jump to main content' and p_tag.text != 'Jump to navigation':
                content += ' ' + p_tag.text
        except:
            pass

    return content

tc = scrape_speeches()