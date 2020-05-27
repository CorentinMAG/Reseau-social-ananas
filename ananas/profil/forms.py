from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
from login.models import Etudiant, Majeure, Campus
from string import Template
from django.contrib.auth import get_user_model
import re
from django.utils.safestring import mark_safe

User = get_user_model()


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


class ProfilForm(forms.Form):
    """Formulaire d'inscription pour les étudiants"""
    avatar = forms.ImageField(widget=PictureWidget)
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom.nom@epfedu.fr', 'id': 'email'}))
    nom = forms.CharField(label="",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom'}))
    prenom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom'}))
    naissance = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'jj/mm/aaaa', 'id': 'naissance'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password1'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification du mot de passe', 'id': 'password2'}))
    majeure = forms.ModelChoiceField(queryset=Majeure.objects.all(), label="",
                                     widget=forms.Select(attrs={'class': 'form-control', 'id': 'majeure'}))
    campus = forms.ModelChoiceField(queryset=Campus.objects.all(), label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'campus'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@epfedu.fr' not in email:
            raise forms.ValidationError('Entrer votre mail epf')
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError('Le mail existe déjà')
        except User.DoesNotExist:
            return email

    def clean_promo(self):
        promo = self.cleaned_data['promo']
        regex = re.compile('^20[0-9]{2}$')
        if not regex.match(promo):
            raise forms.ValidationError('Année non valide')
        return promo

    def clean(self):
        cleaned_data = super(EtudiantForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                self.add_error("password2",
                               "Les mots de passe sont différents !"
                               )
            else:
                if len(password1) < 6:
                    self.add_error("password2",
                                   "le mot de passe est trop court ! ")

        return cleaned_data

    def save(self, commit=True):
        prenom = self.cleaned_data["prenom"]
        password = self.cleaned_data["password1"]
        nom = self.cleaned_data["nom"]
        email = self.cleaned_data["email"]
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password)
        user.is_active = False

        majeure = self.cleaned_data['majeure']
        profilEtudiant = Etudiant(user=user, majeure=majeure)
        profilEtudiant.save()
        if commit:
            user.save()
        return user
