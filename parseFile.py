import requests
from bs4 import BeautifulSoup
from bs4 import Tag, ResultSet
from settings import URL
import datetime

x = str(datetime.datetime.now())
now_date = x[0:-16]

headers = {
    'User-Agent': 'xiaomi_probook_15.6',
    'From': 'esenaliev2304@gmail.com'  # This is another valid field
}
response = requests.get(URL, headers=headers)

def get_html_card():        # Данная функция возвращает все html карты товаров
    html = requests.get(URL+f'/?lable=8&date={now_date}&order=time')
    soup = BeautifulSoup(html.text, 'lxml')
    cards: ResultSet = soup.find_all('div', class_="ArticleItem--data ArticleItem--data--withImage")
    return cards

def parse_cards(cards):
    obj_list = []
    id_ = 0
    for i in cards:
        obj = {
            'link': i.find('a', class_='ArticleItem--name').get('href'),
            'title':i.find('a', class_='ArticleItem--name').text,
            'id': str(id_)
        }
        id_+=1
        obj_list.append(obj)
    return obj_list



def get_news_list():
    return parse_cards(get_html_card())

def parse_news_page(url_):
    html = requests.get(url_)
    soup = BeautifulSoup(html.text, 'lxml')
    cards: ResultSet = soup.find_all('div', class_="BbCode")
    return cards



