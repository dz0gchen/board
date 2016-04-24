#coding:utf-8

from django.contrib import admin
from .models import Advert
from .forms import AdvertForm

#детализации вывода информации по полям модели в админке при редактировании записи
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['header', 'text', 'date_of_creation']
    readonly_fields = ('date_of_creation',)
    form = AdvertForm
   
    def get_readonly_fields(self, request, obj=None):
        if obj: # Editing
            return self.readonly_fields
        return ()
        
admin.site.register(Advert, AdvertAdmin)
