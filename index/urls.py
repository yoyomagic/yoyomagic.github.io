# coding:utf8
from django.conf.urls import url
from .views import *

urlpatterns = [
    # url(r'^post/(?P<id>\d+)/$', Detail, name="blog_detail"),
    # url(r'^home/', home, name="blog_home"),
    url(r'^happy_yule', happy_yule, name="blog_yule"),
    url(r'^happy_youxi', happy_youxi, name="blog_youxi"),
    url(r'^happy_qiuzhi', happy_qiuzhi, name="blog_qiuzhi"),
    url(r'^happy_python', happy_python, name="blog_python"),
    url(r'^happy_dashuju', happy_dashuju, name="blog_dashuju"),
    url(r'^happy_lvyou', happy_lvyou, name="blog_lvyou"),

    url(r'^contact', contact, name="blog_contact"),
    url(r'^about', about, name="blog_about"),
    url(r'', index, name="blog_index"),
]