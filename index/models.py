# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    title = models.CharField(u"娱乐标题",max_length=100)
    category = models.CharField(u"娱乐标签",max_length=50,blank=True)
    pub_date = models.DateTimeField(u"发布日期",auto_now_add = True,editable=True)
    update_date = models.DateTimeField(u"更新日期",auto_now = True,null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"娱乐正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:#按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "娱乐"
        verbose_name_plural = "娱乐"
class Game(models.Model):
    title = models.CharField(u"游戏标题",max_length=100)
    category = models.CharField(u"游戏标签", max_length=50, blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u"更新日期", auto_now=True, null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"游戏正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "游戏"
        verbose_name_plural = "游戏"
class Job(models.Model):
    title = models.CharField(u"职业标题",max_length=100)
    category = models.CharField(u"职业标签", max_length=50, blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u"更新日期", auto_now=True, null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"职业正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "职业"
        verbose_name_plural = "职业"
class Python(models.Model):
    title = models.CharField(u"Python标题",max_length=100)
    category = models.CharField(u"Python标签", max_length=50, blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u"更新日期", auto_now=True, null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"Python正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "Python"
        verbose_name_plural = "Python"
class Bigdata(models.Model):
    title = models.CharField(u"大数据标题",max_length=100)
    category = models.CharField(u"大数据标签", max_length=50, blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u"更新日期", auto_now=True, null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"大数据正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "大数据"
        verbose_name_plural = "大数据"
class Travel(models.Model):
    title = models.CharField(u"旅游标题",max_length=100)
    category = models.CharField(u"旅游标签", max_length=50, blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u"更新日期", auto_now=True, null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"旅游正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "旅游"
        verbose_name_plural = "旅游"
#特色头条
class Header(models.Model):
    title = models.CharField(u"头条标题",max_length=100)
    category = models.CharField(u"旅游标签", max_length=50, blank=True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u"更新日期", auto_now=True, null=True)
    # content = models.TextField(blank=True,null=True)#博客正文
    content = UEditorField(u"旅游正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "头条"
        verbose_name_plural = "头条"
#特色头条
class Headers(models.Model):
    title = models.CharField(u"头条标题",max_length=100)
    content = UEditorField(u"旅游正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        verbose_name = "头条"
        verbose_name_plural = "头条"
#特色头条
class Head(models.Model):
    # title = models.CharField(u"头条标题",max_length=100)
    title = models.TextField(blank=True, null=True)  # 博客正文
    content = UEditorField(u"旅游正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        verbose_name = "头条"
        verbose_name_plural = "头条"



