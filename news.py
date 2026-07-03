import requests
from config import API_KEY

BASE_URL = "https://newsapi.org/v2/everything"


def latest_news():

    params = {
        "q": "Artificial Intelligence",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    return response.json()["articles"]


def search_news(keyword):

    params = {
        "q": keyword,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    return response.json()["articles"]