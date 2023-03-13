from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Электронная почта'}),
            'feedback_text': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Напишите здесь, что думаете о нас'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Электронная почта'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))