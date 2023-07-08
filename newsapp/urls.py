from django.urls import path

from newsapp.views import (LoginUser, RegisterUser, category, contacts,
                           feedback, index, logout_user, post)
from newsapp.api.views import (CategoryListAPIView, NewsCategoryAPIView,
                               NewsListAPIView, NewsRetrieveAPIView)

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('logout/', logout_user, name='logout_user'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('<slug:post_slug>/', post, name='post'),
    path("api/news/", NewsListAPIView.as_view()),
    path("api/news/<slug:slug>/", NewsRetrieveAPIView.as_view()),
    path("api/categories/", CategoryListAPIView.as_view()),
    path("api/category/<slug:slug>", NewsCategoryAPIView.as_view()),
]
