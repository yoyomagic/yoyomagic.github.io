# coding:utf8

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from index.models import Article
from index.models import Game
from index.models import Job
from index.models import Python
from index.models import Bigdata
from index.models import Travel
from index.models import Header
from index.models import Headers
from index.models import Head
from datetime import datetime
from django.http import Http404

# from .forms import CommentForm
from django.http import Http404
import xlwt
from xlwt import *
import xlrd
# Create your views here.
cols0=[]
cols1=[]
headers=[]
def index(request):
    blogs =  Head.objects.all()
    # #读取excel
    # workBook = xlrd.open_workbook('今日头条.xls'.decode('utf-8'))
    # sheet = workBook.sheet_by_name('Sheet1')
    # cols0 = sheet.col_values(0)
    # cols1 = sheet.col_values(1)
    # #连接属性值
    # zipp=zip(cols0,cols1)

    return render(request, 'blog/index.html',locals())
#娱乐八卦
def happy_yule(request):
    homm = Article.objects.all()
    return render(request, 'blog/happy_yule.html',{'homm':homm})
#游戏人生
def happy_youxi(request):
    youxi= Article.objects.all()
    return render(request, 'blog/happy_youxi.html',locals())
#求职福利
def happy_qiuzhi(request):
    return render(request, 'blog/happy_qiuzhi.html')
#python学习之路
def happy_python(request):
    return render(request, 'blog/happy_python.html')
#大数据学习之路
def happy_dashuju(request):
    return render(request, 'blog/happy_dashuju.html')
#旅游之路
def happy_lvyou(request):
    lv=Travel.objects.all()
    return render(request, 'blog/happy_lvyou.html',locals())

def contact(request):

    return render(request, 'blog/contact.html')
def about(request):
    return render(request, 'blog/about.html')