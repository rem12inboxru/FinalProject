

import requests
from django.shortcuts import render
from datetime import datetime
from time import sleep, time
from .models import Data
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# Create your views here.
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


def render_up(request):
    context = {}
    if request.method == 'POST':
        timeframe = request.POST.get("timeframe")
        number_req = request.POST.get("number_req")
        interval = int(timeframe) * int(number_req)
        context = {'interval': interval}
        for i in parser(int(timeframe), int(number_req)):
            Data.objects.create(ticker= i[0], lastprice=i[1], timeframe=i[2], dateevent=i[3])
    return render(request, 'render_up.html', context)

def render_pausa(request):
    return render(request, 'render_pausa.html' )

def render_calc(request):
    lastprices = []
    dateevents = []
    timer1 = time()
    data = Data.objects.all()
    for i in data:
        lastprices.append(i.lastprice)
        dateevents.append(i.dateevent)
    timer2 = time()
    y = timer2 - timer1  # время извлечения всех элементов из базы данных
    z1 = time()
    data1 = Data.objects.get(id=49)
    z2 = time()
    z = z2 - z1    # время извлечения одного элемента
    a1 = time()
    data2 = Data.objects.filter(lastprice__gte=68).all()
    a2 = time()
    a = a2 - a1    # время извлечения элементов с ценой >= 68
    b1 = time()
    Data.objects.all().delete()
    b2 = time()
    b = b2 - b1
    context = {'y': y, 'z': z, 'a': a, 'b': b}
    plt.plot(dateevents, lastprices)
    plt.savefig('static/plot.jpg', format='jpg')


    return render(request, 'render_calc.html', context)