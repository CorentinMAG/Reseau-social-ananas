from django.forms import ModelForm
from django import forms
from .models import Commentaires


class CommentForm(ModelForm):
    class Meta:
        model = Commentaires
        fields = ('contenu_comm',)
