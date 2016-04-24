#coding:utf-8

from django import forms
from .models import Advert

class AdvertForm(forms.ModelForm):
    
    header = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
     
    #настройка, определяющая модель для формы
    class Meta:
        model = Advert
        fields = ['header', 'text'] 