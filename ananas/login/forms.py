<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.forms import ModelForm
=======
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
from .models import Campus, Majeure, Etudiant, Administration
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
import re

User = get_user_model()
<<<<<<< HEAD


class CustomUserCreationForm(UserCreationForm):
=======

GENDER = (
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    )


class CustomUserCreationForm(UserCreationForm):
    """Formulaire de création d'utilisateur dans le site
    d'administration de django"""
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
<<<<<<< HEAD
=======
    """Formulaire de modification d'utilisateur dans le site d'administration
    de django"""
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    class Meta(UserChangeForm):
        model = User
        fields = ('email',)


class Custom_password_reset_form(PasswordResetForm):
<<<<<<< HEAD
=======
    """Formulaire de reset de password,
    on rentre notre email, si c'est un mail
    epf on reçoit un mail à cette adresse"""
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        regex = re.compile('^([a-zA-Z0-9_\-\.]+)@epfedu.fr$')
        if not regex.match(email):
            raise forms.ValidationError('Entrer votre mail epf')
        return email


class Custom_password_reset_form_confirm(SetPasswordForm):
<<<<<<< HEAD
=======
    """Formulaire de changement de mot de passe"""
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}))


class ConnexionForm(forms.Form):
<<<<<<< HEAD
=======
    """Formulaire de connexion au site"""
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
<<<<<<< HEAD
        if '@epfedu.fr' not in email:
=======
        regex = re.compile('^([a-zA-Z0-9_\-\.]+)@?(epfedu|epf).fr$')
        if not regex.match(email):
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
            raise forms.ValidationError('Entrer votre mail epf')
        return email


class AutreForm(forms.Form):
<<<<<<< HEAD
    poste = forms.CharField(max_length=255, label="", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Expliquer votre métier en quelques mots...', 'id': 'poste'}))
    campus = forms.ModelChoiceField(initial=Campus.objects.first(), queryset=Campus.objects.all(), label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_campus_autre'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'autre_email'}))
=======
    """Formulaire pour enregistrer les membres
    de l'administration et les profs"""
    genre=forms.ChoiceField(choices=GENDER,widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_gender'}))
    campus = forms.ModelChoiceField(initial=Campus.objects.first(), queryset=Campus.objects.all(), label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_campus_autre'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom.nom@epf.fr', 'id': 'autre_email'}))
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1_autre'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification password', 'id': 'password2_autre'}))
    nom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom_autre'}))
    prenom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom_autre'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@epf.fr' not in email:
            raise forms.ValidationError('Entrer le mail epf')
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError('Le mail existe déjà')
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        prenom = self.cleaned_data["prenom"]
        nom = self.cleaned_data["nom"]
<<<<<<< HEAD
        poste = self.cleaned_data['poste']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        campus = self.cleaned_data['campus']
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password)
        user.is_active = False
        user.is_etudiant = False
        user.is_autre = True
        profilAutre = Administration(user=user, poste=poste, campus=campus)
=======
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        campus = self.cleaned_data['campus']
        genre=self.cleaned_data["genre"]
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password,genre=genre)
        user.is_active = False
        user.is_etudiant = False
        user.is_autre = True
        profilAutre = Administration(user=user,campus=campus)
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
        profilAutre.save()
        if commit:
            user.save()
        return user


class EtudiantForm(forms.Form):
<<<<<<< HEAD
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
=======
    """Formulaire d'inscription pour les étudiants"""
    genre = forms.ChoiceField(choices=GENDER,
                              widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_gender'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom.nom@epfedu.fr', 'id': 'email'}))
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    nom = forms.CharField(label="",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom'}))
    prenom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification password', 'id': 'password2'}))
    promo = forms.CharField(max_length=4, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Promo', 'id': 'promo'}))
    majeure = forms.ModelChoiceField(initial=Majeure.objects.first(), queryset=Majeure.objects.all(), label="",
                                     widget=forms.Select(attrs={'class': 'form-control', 'id': 'majeure'}))
    campus = forms.ModelChoiceField(initial=Campus.objects.first(), queryset=Campus.objects.all(), label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_campus'}))

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

    def save(self, commit=True):
        prenom = self.cleaned_data["prenom"]
        password = self.cleaned_data["password1"]
        nom = self.cleaned_data["nom"]
        email = self.cleaned_data["email"]
<<<<<<< HEAD
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password)
=======
        genre=self.cleaned_data["genre"]
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password,genre=genre)
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
        user.is_active = False

        promo = self.cleaned_data['promo']
        campus = self.cleaned_data['campus']
        majeure = self.cleaned_data['majeure']
        profilEtudiant = Etudiant(user=user, promo=promo, majeure=majeure, campus=campus)
        profilEtudiant.save()
        if commit:
            user.save()
        return user
