from bs4 import BeautifulSoup
import requests

''' Works for one url but waiting for advice from Eric regarding the api access for amazon 
'''

def get_film_titles(data):
    film_titles = []
    for product_id in data:
        html_txt = requests.get(f"https://www.amazon.com/dp/{product_id}/").text
        with open(html_txt, encoding='Latin1') as fp:
            soup = BeautifulSoup(fp, features="lxml")
        film_titles.append(soup.find(id="productTitle").string)