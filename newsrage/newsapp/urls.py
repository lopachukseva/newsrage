from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('<slug:post_slug>/', post, name='post'),
]
