from django.db import models


# Create your models here.
class Data(models.Model):
    ticker = models.CharField(max_length=10, default='BTC')
    lastprice = models.DecimalField(decimal_places=2, max_digits=20)
    timeframe = models.IntegerField()
    dateevent = models.DateTimeField(max_length=30, auto_now_add=True)
