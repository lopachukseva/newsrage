from .models import *

categories = Category.objects.all()

footer_menu = [
    {'title': 'Контакты', 'path_name': 'contacts'},
    {'title': 'Обратная связь', 'path_name': 'feedback'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = categories
        context['footer_menu'] = footer_menu
        return context
