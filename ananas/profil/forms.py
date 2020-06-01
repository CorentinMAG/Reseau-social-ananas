from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
from login.models import Etudiant, Majeure, Campus
from string import Template
from django.contrib.auth import get_user_model
import re
from django.utils.safestring import mark_safe
from io import BytesIO
from django.core.files import File
from PIL import Image

User = get_user_model()


class ProfilForm(forms.Form):
    """Formulaire d'inscription pour les étudiants"""
    photo = forms.ImageField(required=False)
    nom = forms.CharField(label="",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom'}))
    prenom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom'}))
    naissance = forms.CharField(max_length=10, required=False, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'jj/mm/aaaa', 'id': 'naissance'}))
    password1 = forms.CharField(required=False, label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password1'}))
    password2 = forms.CharField(required=False, label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification du mot de passe', 'id': 'password2'}))
    majeure = forms.ModelChoiceField(required=False, queryset=Majeure.objects.all(), label="",
                                     widget=forms.Select(attrs={'class': 'form-control', 'id': 'majeure'}))
    campus = forms.ModelChoiceField(required=False, queryset=Campus.objects.all(), label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'campus'}))
    poste = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'poste', 'placeholder': 'Entrer votre poste...'}))

    def clean_naissance(self):
        naissance = self.cleaned_data['naissance']
        regex = re.compile('^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
        if naissance == "":
            return naissance
        elif not regex.match(naissance):
            raise forms.ValidationError('Mauvais Format')
        return naissance

    def clean_photo(self):

        """Makes thumbnails of given size from given image"""
        image = self.cleaned_data['photo']

        im = Image.open(image)
        size = 150, 150
        im.thumbnail(size)  # resize image

        thumb_io = BytesIO()  # create a BytesIO object

        im.save(thumb_io, 'JPEG', quality=100)  # save image to BytesIO object

        photo = File(thumb_io, name=image.name)  # create a django friendly File object

        return photo
