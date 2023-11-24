from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True, verbose_name='Аватар')
    about = models.TextField(max_length=500, verbose_name='Информация о пользователе')
