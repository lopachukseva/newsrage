from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from newsapp.models import News, Category

categories = Category.objects.all()

footer_menu = [
    {'title': 'Контакты', 'path_name': 'contacts'},
    {'title': 'Обратная связь', 'path_name': 'feedback'},
]


def index(response):
    posts = News.objects.filter(is_published=True)

    context = {
        'title': 'NEWSRAGE',
        'posts': posts,
        'categories': categories,
        'footer_menu': footer_menu,
    }

    return render(response, 'newsapp/index.html', context=context)


def contacts(response):
    return render(response, 'newsapp/contacts.html')


def feedback(response):
    return render(response, 'newsapp/feedback.html')


def category(response, category_id):
    posts = News.objects.filter(category=category_id).filter(is_published=True)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'NEWSRAGE',
        'posts': posts,
        'categories': categories,
        'footer_menu': footer_menu,
    }

    return render(response, 'newsapp/index.html', context=context)


def post(response, post_id):
    return HttpResponse(f'Пост: {post_id}')


def pageNotFound(response, exception):
    return HttpResponseNotFound(f'<h3>Упс! Кажется, такой страницы не существует, или же она была удалена.</h3>')
