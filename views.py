from typing import Dict, Any

import requests
from django.shortcuts import render
from datetime import datetime
from time import sleep, time
from .models import Data
from .parser1 import parser
import matplotlib.pyplot as plt

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
    data = Data.objects.all()
    for i in data:
        lastprices.append(i.lastprice)
        dateevents.append(i.dateevent)

    plt.plot(dateevents, lastprices)
    plt.savefig('static/plot.jpg', format='jpg')

    return render(request, 'render_calc.html')

def render_calc1(request):
    datas1 = []
    timer1 = time()
    data = Data.objects.all()
    for i in data:
        datas1.append([i.id, i.ticker, i.lastprice, i.timeframe, i.dateevent])
    timer2 = time()
    y = timer2 - timer1
    context = {'y': y, 'datas1': datas1}
    return render(request, 'render_calc1.html', context)

def render_calc2(request):
    context = {}
    if request.method == "POST":
        id = request.POST.get("id")
        id_int = int(id)
        print(id_int)
        datas2 = []
        data = Data.objects.all()
        for i in data:
            datas2.append(i.id)
        if id_int in datas2:
            z1 = time()
            data2 = Data.objects.get(pk=id_int)
            z2 = time()
            z = z2 - z1
        else:
            z = 0
            data2 = 'Нет записи в БД с таким id'
        context = {'z': z, 'data2': data2}
    return render(request, 'render_calc2.html', context)

def render_calc3(request):
    context = {}
    if request.method == "POST":
        lastprice = request.POST.get("lastprice")
        lastprice_fl = float(lastprice)
        print(lastprice_fl)
        data3 = []
        a1 = time()
        data31 = Data.objects.filter(lastprice__gte=lastprice_fl)
        for i in data31:
            data3.append([i.id, i.ticker, i.lastprice, i.timeframe, i.dateevent])
        a2 = time()
        a = a2 - a1
        context = {'a': a, 'data3': data3}
    return render(request, 'render_calc3.html', context)

def render_calc4(request):
    b1 = time()
    Data.objects.all().delete()
    b2 = time()
    b = b2 - b1
    context = {'b': b}
    return render(request, 'render_calc4.html', context)