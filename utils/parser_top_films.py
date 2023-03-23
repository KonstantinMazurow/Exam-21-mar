import requests
from data.config import URL_TOP_FILMS
from bs4 import BeautifulSoup as bs


def get_top_movies():
    r = requests.get(URL_TOP_FILMS)
    soup = bs(r.text, "html.parser")
    data = soup.find('div', class_='entry-content').find_all('strong')
    movies_list = []
    for row in data:
        movies_list.append(row.get_text())
    return (movies_list[0:10])
