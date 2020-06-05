from django.forms import ModelForm
from .models import Commentaires, Article, Tags
from django import forms
from pagedown.widgets import PagedownWidget
from io import BytesIO
from django.core.files import File
from PIL import Image


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


class SearchTag(forms.ModelForm):
    text_tag = forms.ModelChoiceField(initial=Tags.objects.first(), queryset=Tags.objects.all(), label="",
                                  widget=forms.Select(attrs={'class': 'form-control', 'id': 'tags'}))

    class Meta:
        model = Tags
        fields = ('text_tag',)


class ArticleForm(forms.ModelForm):
    titre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre', 'id': 'titre_article'}))
    contenu_post = forms.CharField(widget=PagedownWidget)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'form-control', 'id': 'tags_article'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'id': 'file_article'}))

    class Meta:
        model = Article
        exclude = ('auteur', 'slug')

    def clean_photo(self):

        """Makes thumbnails of given size from given image"""
        image = self.cleaned_data['photo']
        if (image):
            im = Image.open(image)
            size = 200, 200
            im.thumbnail(size)  # resize image
            rgb_im = im.convert('RGB')

            thumb_io = BytesIO()  # create a BytesIO object

            rgb_im.save(thumb_io, 'JPEG', quality=100)  # save image to BytesIO object

            photo = File(thumb_io, name=image.name)  # create a django friendly File object

            return photo
        else:
            return image
