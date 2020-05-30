from django.forms import ModelForm, CharField
from .models import Commentaires, Article
from django import forms


class CommentForm(ModelForm):
    """
    Créer un nouveau commentaire sur un Article,
    lié à timeline/x, x = id article
    """
    contenu_comm=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrer votre commentaire...'}))
    class Meta:
        model = Commentaires
        fields = ('contenu_comm',)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
