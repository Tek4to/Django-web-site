from django.db import models

# Create your models here.
from django.db import models


class Parking(models.Model):
    address = models.CharField(max_length=150, unique=True, verbose_name='Адрес')
    rate = models.FloatField(null=True, verbose_name='Рейтинг')
    count_places = models.IntegerField(verbose_name='Количество мест')
    parking_price = models.IntegerField(verbose_name='Цена за день')
    test_field = models.IntegerField(verbose_name='Цена за день', default=0)

