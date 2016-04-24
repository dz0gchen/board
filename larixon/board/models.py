#coding: utf-8

from __future__ import unicode_literals

from django.db import models

class Advert(models.Model):
         
    header = models.CharField(u'Заголовок', max_length=120, blank=False, null=False)
    text = models.CharField(u'Текст', max_length=120, blank=False, null=False)
    date_of_creation = models.DateField(u'Дата создания', auto_now_add=True, auto_now=False)
        
    def __unicode__(self): 
        #возращает поля, которые отображаются в админке
        return '%s %s %s' % (self.header, self.text, self.date_of_creation)
