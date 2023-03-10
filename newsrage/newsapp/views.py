from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect

from newsapp.models import News, Category, Feedback, Comments

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
    post_comments = Comments.objects.filter(news_id=post.pk)

    context = {
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
        'post_comments': post_comments,
    }
    return render(response, 'newsapp/post.html', context=context)


def contacts(response):
    context = {
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
    }
    return render(response, 'newsapp/contacts.html', context=context)


def feedback(response):
    context = {
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
    }
    return render(response, 'newsapp/feedback.html', context=context)


def pageNotFound(response, exception):
    return render(response, 'newsapp/notfound.html')
