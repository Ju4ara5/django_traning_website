# файл модуля настройки админки
# (нужен для детальной настройки вариантов отображения
# и управления приложениями из админпанели)
from django.contrib import admin

# импортируем приложение в админпанель:
from .models import Order

# регистрируем приложение в админпанели:
# Register your models here.
admin.site.register(Order)

# Register your models here.
