import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep, time


def parser(x, y):
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    k = 0
    data_two = []
    while k <= y:
        ticker = 'BTC'
        response = requests.get(url)
        # отправляем запрос к сайту
        bs = BeautifulSoup(response.text, 'lxml')
        price_btc = bs.find('span', 'sc-65e7f566-0 WXGwg base-text')
        # получили цену BTC с HTML-страницы сайта
        btc = float(price_btc.text[1:].replace(',', ''))
        # приведеник цены в соответствие с полем DecimalField для передачи значения в БД
        dateevent = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # фиксируем время получения цены и тоже приводим в соответствие с полем DateTimeField
        print(dateevent)
        data_one = [ticker, btc, x, dateevent]
        # собираем все данные в список - это строка в БД
        print(data_one)
        data_two.append(data_one)
        # собираем все полученные данные за промежуток времени
        sleep(x * 60)
        # выдерживаем паузу, чтобы не перегружать сайт запросами с нашего адреса
        # если не делать паузы между запросами, сайт перестает отвечать
        k += 1
    print(data_two)
    return data_two
