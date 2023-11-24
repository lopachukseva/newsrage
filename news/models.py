from django.db import models
from django.urls import reverse

from users.models import User


class News(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Главная фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=40, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CommentsQuerySet(models.QuerySet):
    def total_count(self):
        return len(self)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    comment = models.TextField(blank=True, verbose_name='Текст комментария')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время написания')
    news = models.ForeignKey('News', on_delete=models.SET_NULL, null=True, verbose_name='Пост')

    objects = CommentsQuerySet.as_manager()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.CharField(max_length=50, verbose_name='Электронная почта')
    feedback_text = models.TextField(blank=True, verbose_name='Текст обратной связи')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
