#Импорты
from bs4 import BeautifulSoup
import requests

#Функция, собирающая информацию с сайта РИА Новости
def DataFrame():
    
    #Создаётся словарь с новостью, ссылкой, кол-вом просмотров и датой публикации.
    dict_news = {"news": [], "links": [], "views": [], "date": []}
    
    # Это URL-адрес веб-страницы, с которой мы хотим получить данные.
    url = "https://ria.ru/keyword_globalnoe_poteplenie/"
    
    #Отправляется GET-запрос
    response = requests.get(url)

    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find_all('div', 'list-item')
    for i in temp:
        dict_news["news"].append(i.find('a','list-item__title color-font-hover-only').text)
        dict_news["links"].append(i.find('a').get('href'))
        dict_news["views"].append(i.find('div','list-item__views-text').text)
        dict_news["date"].append(i.find('div','list-item__date').text)
    return dict_news
print(DataFrame()['news'][0])