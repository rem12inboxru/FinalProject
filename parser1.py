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
        bs = BeautifulSoup(response.text, 'lxml')
        price_btc = bs.find('span', 'sc-65e7f566-0 WXGwg base-text')
        btc = float(price_btc.text[1:].replace(',', ''))
        dateevent = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        print(dateevent)
        data_one = [ticker, btc, x, dateevent]
        print(data_one)
        data_two.append(data_one)
        sleep(x * 60)
        k+=1
    print(data_two)
    return data_two