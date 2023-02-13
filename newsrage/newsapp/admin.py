from django.contrib import admin

from newsapp.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_create', 'is_published', 'category')
    search_fields = ['title']
    list_editable = ['is_published']
    list_filter = ['is_published']
    empty_value_display = '-empty-'
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
