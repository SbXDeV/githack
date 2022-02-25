from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=100)

    def __str__(self):
        return self.title


class Content(models.Model):
    """ Содержание сайта """
    image = models.ImageField(upload_to='media/', verbose_name='Обложка поста')
    title = models.CharField(verbose_name='Заголовок статьи', max_length=300)
    short_content = models.TextField(verbose_name='Короткое содержание поста')
    content = models.TextField(verbose_name='Содержание поста')
    author = models.CharField(verbose_name='Автор поста', max_length=100, default='SVDe')
    category = models.ManyToManyField(Category, verbose_name='Категория поста')
    date = models.DateTimeField(verbose_name='Время публикации')

    class Meta:
        verbose_name = 'посты'
        verbose_name_plural = 'пост'

    def __str__(self):
        return 'Пост:' + self.title
