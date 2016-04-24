#coding: utf-8

from .models import Advert
from django.views.generic import ListView, DetailView

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

    def get_object(self):
        obj = super(Detail, self).get_object()
        return obj