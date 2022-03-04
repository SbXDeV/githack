from django.db import models


class News(models.Model):
    """ Новости """
    image = models.ImageField(upload_to='media/', verbose_name='Обложка поста')
    title = models.CharField(verbose_name='Заголовок статьи', max_length=300)
    short_content = models.TextField(verbose_name='Короткое содержание поста')
    content = models.TextField(verbose_name='Содержание поста')
    author = models.CharField(verbose_name='Автор поста', max_length=100, default='SVDe')
    date = models.DateTimeField(verbose_name='Время публикации')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return 'Новость:' + self.title


class Tools(models.Model):
    """ Инструменты """
    image = models.ImageField(upload_to='media/', verbose_name='Обложка поста')
    title = models.CharField(verbose_name='Заголовок статьи', max_length=300)
    short_content = models.TextField(verbose_name='Короткое содержание поста')
    content = models.TextField(verbose_name='Содержание поста')
    author = models.CharField(verbose_name='Автор поста', max_length=100, default='SVDe')
    date = models.DateTimeField(verbose_name='Время публикации')

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return 'Инструмент:' + self.title


class Guid(models.Model):
    """ Гайд """
    image = models.ImageField(upload_to='media/', verbose_name='Обложка поста')
    title = models.CharField(verbose_name='Заголовок статьи', max_length=300)
    short_content = models.TextField(verbose_name='Короткое содержание поста')
    content = models.TextField(verbose_name='Содержание поста')
    author = models.CharField(verbose_name='Автор поста', max_length=100, default='SVDe')
    date = models.DateTimeField(verbose_name='Время публикации')

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'

    def __str__(self):
        return 'Инструкция:' + self.title
