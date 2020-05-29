from django.forms import ModelForm, CharField
from .models import Commentaires, Article
from django import forms


class CommentForm(ModelForm):
    """
    Créer un nouveau commentaire sur un Article,
    lié à timeline/x, x = id article
    """

    class Meta:
        model = Commentaires
        fields = ('contenu_comm',)


class ArticleForm(forms.ModelForm):
    contenu_post = forms.CharField(widget=forms.Textarea(attrs={'cols': "200"}))

    class Meta:
        model = Article
        fields = '__all__'




