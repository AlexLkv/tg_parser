import requests
import results as results
from bs4 import BeautifulSoup



def pars(url):


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    x = soup.find("a", class_="tgme_widget_message_photo_wrap")
    l = soup.find("meta", property="og:image")
    return x["content"], l["content"]
response = requests.get('https://t.me/lopppppaq/23?embed=1&mode=tme')
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.find("video").get('src'))
print((soup.find('a', "tgme_widget_message_photo_wrap").get("style").split("'")[1]))