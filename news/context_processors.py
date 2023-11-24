from news.models import Category


def categories(request):
    return {
        "categories": Category.objects.all(),
    }


def footer(request):
    return {
        "footer_menu": [
            {'title': 'Контакты', 'path_name': 'contacts'},
            {'title': 'Обратная связь', 'path_name': 'feedback'},
        ]}
