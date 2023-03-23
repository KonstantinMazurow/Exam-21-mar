from data.config import LINK_CAT
import requests


def get_pictures_cat():
    r = requests.get(LINK_CAT)
    data = r.json()
    return data[0]['url']
