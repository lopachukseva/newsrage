from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title
