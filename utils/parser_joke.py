import requests
from bs4 import BeautifulSoup as bs
from data.config import URL_JOKE


def get_joke():
    r = requests.get(URL_JOKE)
    soup = bs(r.text, "html.parser")
    joke = str(soup.find('table', class_='text').text)
    return joke
