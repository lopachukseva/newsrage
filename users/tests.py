from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse("register_user")
        self.data = {
            "first_name": "Anonym",
            "last_name": "User",
            "username": "anonymuser",
            "email": "anonymuser@test.com",
            "password1": "Gb91t78YuTGG",
            "password2": "Gb91t78YuTGG",
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "NEWSRAGE - Регистрация")
        self.assertTemplateUsed(response, "users/register.html")

    def test_user_registration_post(self):
        username = self.data["username"]

        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("login_user"))
        self.assertTrue(User.objects.filter(username=username).exists())
