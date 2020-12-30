from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
from .models import Campus, Majeure, Etudiant, Administration
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
import re

User = get_user_model()
MAIL = '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9]+)\.([a-z]{2,})$'


class CustomUserCreationForm(UserCreationForm):
    
    """
    Form to create a User in the django admin panel site
    """

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    
    """
    Form to chango info about a specific user in the django admin panel site
    """

    class Meta(UserChangeForm):
        model = User
        fields = ('email',)


class Custom_password_reset_form(PasswordResetForm):
    
    """
    this form allows a user to reset his password
    """

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Email'}))
    
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        regex = re.compile(MAIL)
        if not regex.match(email):
            raise forms.ValidationError('Entrer un mail correct ')
        return email


class Custom_password_reset_form_confirm(SetPasswordForm):
    """Formulaire de changement de mot de passe"""
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}))


class ConnexionForm(forms.Form):
    """connexion form"""
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password'}))
    stay_connected = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(
        attrs={'class': 'onoffswitch-checkbox', 'id': 'myonoffswitch'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        regex = re.compile(MAIL)
        if not regex.match(email):
            raise forms.ValidationError('Entrer un mail correct')
        return email


class AutreForm(forms.Form):
    """Formulaire pour enregistrer les membres
    de l'administration et les profs"""
    campus = forms.ModelChoiceField(empty_label=None, queryset=None, label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_campus_autre'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom.nom@example.fr', 'id': 'autre_email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1_autre'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification password', 'id': 'password2_autre'}))
    nom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom_autre'}))
    prenom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom_autre'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campus'].queryset = Campus.objects.all()

    class Meta:
        model = Administration
        fields = ('prenom', 'nom', 'password1', 'password2', 'email', 'campus')

    def clean_email(self):
        email = self.cleaned_data['email']
        regex = re.compile(MAIL)
        if not regex.match(email):
            raise forms.ValidationError('Entrer un mail correct ')
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError('Le mail existe déjà')
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        prenom = self.cleaned_data["prenom"]
        nom = self.cleaned_data["nom"]
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        campus = self.cleaned_data['campus']
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password, campus=campus)
        user.is_active = False
        user.is_etudiant = False
        user.is_autre = True
        profilAutre = Administration(user=user)
        profilAutre.save()
        if commit:
            user.save()
        return user


class EtudiantForm(UserCreationForm):
    """Formulaire d'inscription pour les étudiants"""
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom.nom@example.fr', 'id': 'email'}))
    nom = forms.CharField(label="",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom'}))
    prenom = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom'}))
    campus = forms.ModelChoiceField(empty_label=None, queryset=None, label="",
                                    widget=forms.Select(
                                        attrs={'class': 'form-control', 'id': 'select_campus_etudiant'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password1'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification du mot de passe', 'id': 'password2'}))
    majeure = forms.ModelChoiceField(empty_label=None, queryset=None, label="",
                                     widget=forms.Select(attrs={'class': 'form-control', 'id': 'majeure'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campus'].queryset = Campus.objects.all()
        self.fields['majeure'].queryset = Majeure.objects.all()

    class Meta:
        model = User
        fields = ('majeure', 'password1', 'password2', 'nom', 'prenom', 'email', 'campus')

    def clean_email(self):
        email = self.cleaned_data['email']
        regex = re.compile(MAIL)
        if not regex.match(email):
            raise forms.ValidationError('Entrer un mail correct ')
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError('Le mail existe déjà')
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        prenom = self.cleaned_data["prenom"]
        password = self.cleaned_data["password1"]
        nom = self.cleaned_data["nom"]
        email = self.cleaned_data["email"]
        campus = self.cleaned_data['campus']
        user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password, campus=campus)
        user.is_active = False

        majeure = self.cleaned_data['majeure']
        profilEtudiant = Etudiant(user=user, majeure=majeure)
        profilEtudiant.save()
        if commit:
            user.save()
        return user
