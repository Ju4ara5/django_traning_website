# хранятся модели приложения  (инструкция для формирования данных в базе данных)
# модели отвечают за работу с данными, за управление, хранение, и манипуляцию с ними
# модели это представление таблицы в базе данных и её полей средствами пайтон

# здесь описываются атрибуты модели - соответствующие поля в таблице базы данных

# Create your models here.

from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

# метод строкового представления обекта данных:
    def __str__(self):
        return self.order_name


# переводитм order и orders на русский. добавлением субкласса мета,
# с указанием verbose_name= в единственном числе и verbose_name_plural= во множественном:
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
