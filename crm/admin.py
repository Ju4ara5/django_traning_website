# файл модуля настройки админки
# (нужен для детальной настройки вариантов отображения
# и управления приложениями из админпанели)
from django.contrib import admin

# импортируем приложение в админпанель:
from .models import Order, StatusCrm, ComentCrm

# регистрируем приложение в админпанели:
# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)

# Register your models here.
