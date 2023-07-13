from django.urls import path

from users.views import LoginUser, RegisterUser, logout_user

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login_user'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('logout/', logout_user, name='logout_user'),
]