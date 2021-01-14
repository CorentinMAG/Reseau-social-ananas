from django.forms import ModelForm
from .models import Comment, Article, Tags
from django import forms
from pagedown.widgets import PagedownWidget
from mdeditor.fields import MDTextFormField
from io import BytesIO
from django.core.files import File
from PIL import Image


class CommentForm(ModelForm):
    """
    Créer un nouveau commentaire sur un Article,
    lié à timeline/x, x = id article
    """
    contenu_comm = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Entrer votre commentaire...', 'rows': '3'}))

    class Meta:
        model = Comment
        fields = ('content',)


class AddTags(forms.ModelForm):
    text_tag = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du tag...'}))
    type_tag = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type du tag...'}))

    class Meta:
        model = Tags
        fields = '__all__'


class SearchTag(forms.ModelForm):
    text_tag = forms.ModelChoiceField(initial=Tags.objects.filter(text_tag='Tous les tags'),
                                      to_field_name='text_tag',
                                      queryset=None, label="",empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-control', 'id': 'tags'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_tag'].queryset = Tags.objects.all()

    class Meta:
        model = Tags
        fields = ('text_tag',)


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'id': 'titre_article'}))
    # content = MDTextFormField()
    # tags = forms.ModelMultipleChoiceField(queryset=None,
    #                                       widget=forms.SelectMultiple(
    #                                           attrs={'class': 'form-control', 'id': 'tags_article'}))
    # photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'id': 'file_article'}))

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['tags'].queryset = Tags.objects.exclude(type_tag = 'invisible')
    photo = forms.ImageField()

    class Meta:
        model = Article
        exclude = ['publisher', 'slug','modified']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'id': 'titre_article'}),
            'tags':forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'tags_article'}),
            'content':MDTextFormField(),
        }

    def clean_photo(self):

        """Makes thumbnails of given size from given image"""
        image = self.cleaned_data['photo']
        # if (image):
        #     im = Image.open(image)
        #     size = 900, 300
        #     im.thumbnail(size)  # resize image
        #     rgb_im = im.convert('RGB')
        #
        #     thumb_io = BytesIO()  # create a BytesIO object
        #
        #     rgb_im.save(thumb_io, 'JPEG', quality=100)  # save image to BytesIO object
        #
        #     photo = File(thumb_io, name=image.name)  # create a django friendly File object
        #
        #     return photo
        # else:
        return image
