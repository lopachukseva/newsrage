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


def category(response, category_slug):
    category = Category.objects.get(slug=category_slug)

    posts = News.objects.filter(category=category.pk).filter(is_published=True)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'NEWSRAGE',
        'posts': posts,
        'categories': categories,
        'footer_menu': footer_menu,
    }

    return render(response, 'newsapp/index.html', context=context)


def post(response, post_slug):
    post = News.objects.get(slug=post_slug)

    context = {
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
    }
    return render(response, 'newsapp/post.html', context=context)


def pageNotFound(response, exception):
    return render(response, 'newsapp/notfound.html')
