from django.contrib import admin

from newsapp.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_create', 'is_published', 'category')
    fields = ('title', 'content', 'photo', ('time_create', 'time_update'), 'is_published', 'category', ('slug', 'id'))
    readonly_fields = ('time_create', 'time_update', 'id')
    search_fields = ['title']
    list_editable = ['is_published']
    list_filter = ['is_published']
    empty_value_display = '-empty-'
    prepopulated_fields = {'slug': ('title',)}



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'time_create', 'news')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Image, ImageAdmin)
