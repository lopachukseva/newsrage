from .models import *

categories = Category.objects.all()


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        return context
