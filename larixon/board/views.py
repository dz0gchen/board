#coding: utf-8

import os
import re
from .models import Advert
from django.views.generic import ListView, DetailView

#c:\Program Files\Redis>redis-server --service-start redis.windows-service.conf --sentinel
import redis
from django.conf import settings
cache = redis.StrictRedis(host=settings.REDIS_HOST,
                          port=settings.REDIS_PORT,
                          db=settings.REDIS_DB)

class Index(ListView):    
    model = Advert
    paginate_by = 2
    context_object_name = 'index'   
    template_name = 'index.html'
    
#детализация объявления
class Detail(DetailView):
    model = Advert
    context_object_name = 'detail'
    template_name = 'detail.html'
    
    def dispatch(self, request, *args, **kwargs):
                 
        pattern =  r'\d+'
        url = request.get_full_path()
        result = re.search(pattern, url)
        id = result.group(0)
        
        key = str(request.META['HTTP_USER_AGENT'] + request.META['REMOTE_ADDR'] + id)
        #cache.flushall()
        
        #если ключ уже существует ничего не делаем
        if cache.get(key):
            pass
        else:
            #добавляем ключ, значение ключа не играет роли
            cache.append(key, id)            
            #ключ будет жить в хранилище сутки
            cache.expire(key, 86400)
            #если для id уже ведется счетчик - инкрементируем
            if cache.get(id):
                cache.incr(id)
            else:
                #создаем счетчик для id
                cache.append(id, 1)
                 
        return super(Detail, self).dispatch(request, *args, **kwargs)
    
    def get_object(self):
        obj = super(Detail, self).get_object()
        return obj