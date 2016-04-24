#coding:utf-8

"""larixon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from board.views import Index, Detail
# в urlpatterns необходимо использовать одно представление два раза, но без добавления url(r'^index/$', Index.as_view()),
# url(r'^index/(?P<page>\d+)/$', Index.as_view()), не работает. Такой подход описан в http://djbook.ru/rel1.7/topics/http/urls.html
#.....Значения по умолчанию для аргументов представления
urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^index/$', Index.as_view()),
    url(r'^index/(?P<page>\d+)/$', Index.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', Detail.as_view()),
    url(r'^admin/', admin.site.urls),
]