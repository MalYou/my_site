from django.contrib import admin

from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'date',)
    list_display_links = ('id', 'title',)
    list_filter = ('slug', 'author',)
    prepopulated_fields = {
        'slug': ('title',)
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user_name', 'post',)
    list_display_links = ('id',)

admin.site.register(models.Tag)
admin.site.register(models.Author)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
