from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:category_id>/', categories),
]
