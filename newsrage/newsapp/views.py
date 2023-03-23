from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FeedbackForm, RegisterUserForm, LoginUserForm, CommentsForm
from newsapp.models import News, Category, Feedback, Comments
from .utils import DataMixin

categories = Category.objects.all()

footer_menu = [
    {'title': 'Контакты', 'path_name': 'contacts'},
    {'title': 'Обратная связь', 'path_name': 'feedback'},
]


def index(request):
    posts = News.objects.filter(is_published=True)

    context = {
        'title': 'NEWSRAGE',
        'posts': posts,
        'categories': categories,
        'footer_menu': footer_menu,
    }

    return render(request, 'newsapp/index.html', context=context)


def category(request, category_slug):
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

    return render(request, 'newsapp/index.html', context=context)


def post(request, post_slug):
    post = News.objects.get(slug=post_slug)
    post_comments = Comments.objects.filter(news_id=post.pk)
    this_url = f'post/{post.slug}/'

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            print(request.POST)
            new_comment = form.save(commit=False)
            new_comment.news = post
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = CommentsForm()

    context = {
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
        'post_comments': post_comments,
        'form': form,
        'this_url': this_url,
    }

    print(request)

    return render(request, 'newsapp/post.html', context=context)


def contacts(request):
    context = {
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
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
        'title': 'NEWSRAGE',
        'post': post,
        'categories': categories,
        'footer_menu': footer_menu,
        'form': form,
    }
    return render(request, 'newsapp/feedback.html', context=context)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'newsapp/login.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context()
        return dict(list(context.items()) + list(user_context.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'newsapp/register.html'
    success_url = reverse_lazy('login_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context()
        return dict(list(context.items()) + list(user_context.items()))


def logout_user(request):
    logout(request)
    return redirect('index')


def pageNotFound(response, exception):
    return render(response, 'newsapp/notfound.html')

# class Index(DataMixin, ListView):
#     model = News
#     template_name = 'newsapp/index.html'
#     context_object_name = 'news'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_context = self.get_user_context()
#         return dict(list(context.items()) + list(user_context.items()))
#
#     def get_queryset(self):
#         return News.objects.filter(is_published=True)
