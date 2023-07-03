from django.urls import path
from .views import *
from .views_api import NewsAPIList, NewsAPIDetailView

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('logout/', logout_user, name='logout_user'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('<slug:post_slug>/', post, name='post'),
    path("api/news/", NewsAPIList.as_view()),
    path("api/news/<int:pk>", NewsAPIDetailView.as_view()),
]
