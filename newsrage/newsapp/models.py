from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/", verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

        ordering=['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
