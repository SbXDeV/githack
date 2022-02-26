import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from index.models import Content


class Index(ListView):
    """ Главная страница сайта """
    template_name = 'index/index.html'
    model = Content
    context_object_name = 'contents'

    def get(self, request):
        news = Content.objects.order_by('-date').filter(category__title='Новости')[0:4]
        tools = Content.objects.order_by('-date').filter(category__title='Инструменты')[0:4]

        context = {
            'news': news,
            'tools': tools
        }
        return render(request, self.template_name, context)


class Tool(ListView):
    """ Страница просмотра Инструментов """
    template_name = 'index/tools.html'
    model = Content
    context_object_name = 'contents'


class News(ListView):
    """ Страница просмотра Новостей """
    template_name = 'index/news.html'
    model = Content
    context_object_name = 'contents'


class Guide(ListView):
    """ Страница просмотра Инструкций """
    template_name = 'index/lesson.html'
    model = Content
    context_object_name = 'contents'


class Detail(DetailView):
    """ Детальный просмотр поста """
    template_name = 'index/detail.html'
    model = Content
    context_object_name = 'contents'
