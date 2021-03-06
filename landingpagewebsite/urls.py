"""Этот файл отвечает за маршрутизацию запросов (файл URL-привязок),
   прописываются пути к нашим функциям вызова (пути к функциям views),
   'когда запрос поступает на определённый адрес, этот файл (urls.py) обрабатывает данный запрос
   и переключать данный запрос на нужную вьюху'
"""

"""landingpagewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.first_page),
                  path('thanks/', views.thanks_page, name='thanks_page')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
