from django.forms import ModelForm, CharField
from .models import Commentaires, Article


class CommentForm(ModelForm):
    """
    Créer un nouveau commentaire sur un Article,
    lié à timeline/x, x = id article
    """

    class Meta:
        model = Commentaires
        fields = ('contenu_comm',)


class ArticleForm(ModelForm):
    article_content = CharField()

    class Meta:
        model = Article
        fields = ('contenu_post',)
