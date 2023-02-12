from django.contrib import admin

from newsapp.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo', 'time_create', 'is_published', 'category')
    search_fields = ['title']
    list_editable = ['is_published']
    empty_value_display = '-empty-'


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
