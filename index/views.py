import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class Index(ListView):
    """ Главная страница сайта """
    template_name = 'index/index.html'

    def get(self, request):
        news = models.News.objects.order_by('-date')[0:4]
        tools = models.Tools.objects.order_by('-date')[0:4]

        context = {
            'news': news,
            'tools': tools
        }
        return render(request, self.template_name, context)


class Tool(ListView):
    """ Страница просмотра Инструментов """
    template_name = 'index/tools.html'
    model = models.Tools
    context_object_name = 'contents'


class News(ListView):
    """ Страница просмотра Новостей """
    template_name = 'index/news.html'
    model = models.News
    context_object_name = 'contents'


class Guide(ListView):
    """ Страница просмотра Инструкций """
    template_name = 'index/lesson.html'
    model = models.Guid
    context_object_name = 'contents'


# Детальный просмотр
class DetailNews(DetailView):
    """ Детальный просмотр Новостей """
    template_name = 'index/detail.html'
    model = models.News
    context_object_name = 'contents'


class DetailTools(DetailView):
    """ Детальный просмотр Инструментов """
    template_name = 'index/detail.html'
    model = models.Tools
    context_object_name = 'contents'


class DetailGuid(DetailView):
    """ Детальный просмотр Инструкций """
    template_name = 'index/detail.html'
    model = models.Guid
    context_object_name = 'contents'
