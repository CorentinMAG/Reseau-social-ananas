from django.contrib import admin
from django.utils.text import Truncator

from .models import Article, Tags, Commentaires


class ArticleAdmin(admin.ModelAdmin):
    """
    Personnalise l'affichage des articles dans l'interface admin
    """
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre',)

    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(article.contenu_post).chars(40, truncate='...')


class CommentairesAdmin(admin.ModelAdmin):
    list_display = ('id_post', 'contenu_comm', 'date_comm',)

    list_filter = ('date_comm',)
    date_hierarchy = 'date_comm'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags)
admin.site.register(Commentaires, CommentairesAdmin)
