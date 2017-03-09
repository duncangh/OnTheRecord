# Base Recurse.py
# Build a website tree diagram from the ground up
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def href_extractor(x):
    """
    :param x: A data point in the Series holding the <a> tags
    :return: Either the relative path of the link or None
    """

    try:
        if x['href'].startswith('/'):
            return x['href']
        return None
    except:
        return None

def get_all_links(page):
    """

    :param page: URL of webpage
    :return: Unique List of Links Found on Page
    """

    links = BeautifulSoup(get(page).content, 'lxml').find_all('a')
    link_ser = pd.Series(links)
    return link_ser.apply(lambda x: href_extractor(x)).dropna().unique()


class Parse:

    def __init__(self, name, url):
        self.name = name
        self.url = url

        self.links = self.get_all_links()

        self.full_links = self.recurse_sub_links()

    def get_all_links(self, url=None):
        """
        :param self.url: URL of webpage
        :return: Unique List of Links Found on Page
        """
        if url == None:
            links = BeautifulSoup(get(self.url).content, 'lxml').find_all('a')
        else:
            links = BeautifulSoup(get(url).content, 'lxml').find_all('a')

        link_ser = pd.Series(links)
        return link_ser.apply(lambda x: self.href_extractor(x)).dropna().unique()

    def recurse_sub_links(self, existing_links=None):
        if existing_links == None:
            existing_links = self.links

        master_links = []
        for link in existing_links:
            full_link = self.url + link
            new_links = self.get_all_links(full_link)

            master_links = np.unique(np.concatenate([master_links, new_links]))

        return master_links

    def href_extractor(self, x):
        """
        :param x: A data point in the Series holding the <a> tags
        :return: Either the relative path of the link or None
        """

        try:
            if x['href'].startswith('/'):
                return x['href']
            return None
        except:
            return None








