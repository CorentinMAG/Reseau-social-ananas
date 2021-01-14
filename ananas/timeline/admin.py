from django.contrib import admin
from django.utils.text import Truncator

from .models import Article, Tags, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    """
    Article view in the django admin site
    """

    readony_fields = [
        'date',
        'modified'
    ]

    list_display = ('title', 'publisher', 'date', 'truncated_post')

    list_filter = ('publisher','date')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }


    fieldsets = (
        (None, {'fields': ('title','publisher','post','photo')}),
        ('Information', {'fields': ('tags', 'slug')}),
    )

    def truncated_post(self, article):

        """
        Return the first 40 characters of the article followed by
        ... if the text is longer
        """

        return Truncator(article.post).chars(40, truncate='...')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('content', 'date',)

    list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(Tags)
