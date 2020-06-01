from django.forms import ModelForm, CharField
from .models import Commentaires, Article
from django import forms
from .models import Commentaires, Article, Tags
from django import forms
from pagedown.widgets import PagedownWidget


class CommentForm(ModelForm):
    """
    Créer un nouveau commentaire sur un Article,
    lié à timeline/x, x = id article
    """
    contenu_comm = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Entrer votre commentaire...'}))

    class Meta:
        model = Commentaires
        fields = ('contenu_comm',)


class AddTags(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    titre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre', 'id': 'titre_article'}))
    contenu_post = forms.CharField(widget=PagedownWidget)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'form-control', 'id': 'tags_article'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'id': 'file_article'}))

    class Meta:
        model = Article
        exclude = ('auteur',)
