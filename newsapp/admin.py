from django.contrib import admin

from newsapp.models import Category, Comments, Feedback, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_create', 'is_published', 'category')
    fields = ('title', 'content', 'photo', ('time_create', 'time_update'), 'is_published', 'category', ('slug', 'id'))
    readonly_fields = ('time_create', 'time_update', 'id')
    search_fields = ['title']
    list_editable = ['is_published']
    list_filter = ['is_published']
    empty_value_display = '-empty-'
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'time_create', 'news')
