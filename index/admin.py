# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from index.models import Article
from index.models import Game
from index.models import Job
from index.models import Python
from index.models import Bigdata
from index.models import Travel
from index.models import Header
from index.models import Headers
from index.models import Head

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class PythonAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class BigdataAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class TravelAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class HeadersAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
class HeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')



admin.site.register(Article,ArticleAdmin)
admin.site.register(Game,GameAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Python,PythonAdmin)
admin.site.register(Bigdata,BigdataAdmin)
admin.site.register(Travel,TravelAdmin)
admin.site.register(Header,HeaderAdmin)
admin.site.register(Headers,HeadersAdmin)
admin.site.register(Head,HeadAdmin)