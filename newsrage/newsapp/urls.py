from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('category/<int:category_id>/', category, name='category'),
    path('<int:post_id>/', post, name='post'),
]
