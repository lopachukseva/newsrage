from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(response):
    return HttpResponse('Стартовая страница сайта')


def categories(response, category_id):
    return HttpResponse(f'Категория новостей: {category_id}')


def pageNotFound(response, exception):
    return HttpResponseNotFound(f'<h3>Упс! Кажется, такой страницы не существует, или же она была удалена.</h3>')