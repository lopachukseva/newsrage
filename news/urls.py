from django.urls import path

from news.api.views import (CategoryListAPIView, NewsCategoryAPIView,
                               NewsListAPIView, NewsRetrieveAPIView)
from news.views import category, contacts, feedback, index, post

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('<slug:post_slug>/', post, name='post'),
    path("api/news/", NewsListAPIView.as_view()),
    path("api/news/<slug:slug>/", NewsRetrieveAPIView.as_view()),
    path("api/categories/", CategoryListAPIView.as_view()),
    path("api/category/<slug:slug>", NewsCategoryAPIView.as_view()),
]
