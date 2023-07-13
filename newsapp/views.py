from django.http import Http404
from django.shortcuts import redirect, render

from newsapp.forms import CommentsForm, FeedbackForm
from newsapp.models import Category, Comments, News


def index(request):
    posts = News.objects.filter(is_published=True)

    context = {
        'title': 'NEWSRAGE - Главная',
        'posts': posts,
    }

    return render(request, 'newsapp/index.html', context=context)


def category(request, category_slug):
    page_category = Category.objects.get(slug=category_slug)
    posts = News.objects.filter(category=page_category.pk).filter(is_published=True)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': f'NEWSRAGE - {page_category.name}',
        'posts': posts,
    }

    return render(request, 'newsapp/index.html', context=context)


def post(request, post_slug):
    post = News.objects.get(slug=post_slug)
    post_comments = Comments.objects.filter(news_id=post.pk).select_related("user")

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.news = post
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentsForm()

    context = {
        'title': f'NEWSRAGE - {post.title}',
        'post': post,
        'post_comments': post_comments,
        'form': form,
    }

    return render(request, 'newsapp/post.html', context=context)


def contacts(request):
    context = {
        'title': 'NEWSRAGE',
        'post': post,
    }

    return render(request, 'newsapp/contacts.html', context=context)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка отправки обратной связи')

    form = FeedbackForm()

    context = {
        'title': 'NEWSRAGE - Обратная связь',
        'post': post,
        'form': form,
    }
    return render(request, 'newsapp/feedback.html', context=context)


def pageNotFound(response, exception):
    return render(response, 'newsapp/notfound.html')
