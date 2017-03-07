# Read all official white house statements
import requests
from bs4 import BeautifulSoup

class Briefings:
    sections = ['https://www.whitehouse.gov/briefing-room/press-briefings',
                'https://www.whitehouse.gov/briefing-room/speeches-and-remarks',
                'https://www.whitehouse.gov/briefing-room/statements-and-releases',
                'https://www.whitehouse.gov/briefing-room/presidential-actions',
                'https://www.whitehouse.gov/briefing-room/legislation',
                'https://www.whitehouse.gov/briefing-room/nominations-and-appointments',
                'https://www.whitehouse.gov/briefing-room/disclosures']


    def __init__(self):
        self.one = 1


    def loop_sections(self):



    def scrape_speeches(self):
        """Scrape all of the speeches available on the White House Page"""
        # Dictionary holding the title of speech/address : content of it
        title_content = {}

        # Todo: Make dyanmic -- so can handle various length pages
        for section in self.sections:


            base_url = section

            resp = requests.get(base_url)
            soup = BeautifulSoup(resp.content, 'lxml')

            links = soup.find('div', {'class': 'view-content'}).find_all('a')

            for link in links:
                speech_url = 'https://www.whitehouse.gov%s' % link['href']
                title_content[speech_url] = self.extract_text(speech_url)

        return title_content

    def extract_text(self, url):
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