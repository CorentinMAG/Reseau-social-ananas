from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordResetForm,SetPasswordForm
from django import forms
from django.forms import ModelForm
from .models import UserProfile,Campus,Majeures
from django.contrib.auth import get_user_model
import re
import datetime

User=get_user_model()

class Custom_password_reset_form(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','autofocus': 'autofocus','placeholder':'Email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        regex=re.compile('^([a-zA-Z0-9_\-\.]+)@epfedu.fr$')
        if not regex.match(email):
            raise forms.ValidationError('Entrer votre mail epf')
        return email

class Custom_password_reset_form_confirm(SetPasswordForm):
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Nouveau mot de passe'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmer le mot de passe'}))


class ConnexionForm(ModelForm):
    class Meta:
        model=User
        fields=['email','password']
        widgets={
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password','id': 'password',})
        }

    def clean_email(self):
    	email=self.cleaned_data['email']
    	if '@epfedu.fr' not in email:
    		raise forms.ValidationError('Entrer votre mail epf')
    	return email


class RegisterForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','id':'email'}))
    username=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','id':'username'}))
    nom=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nom','id':'nom'}))
    prenom=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Prénom','id':'prenom'}))
    password1=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','id':'password1'}))
    password2=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Vérification password','id':'password2'}))
    promo=forms.IntegerField(label="",max_value=9999,min_value=datetime.datetime.now().year,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Promo','id':'promo'}))
    majeure=forms.ModelChoiceField(initial=Majeures.objects.first(),queryset=Majeures.objects.all(),label="",widget=forms.Select(attrs={'class':'form-control','id':'majeure'}))
    naissance=forms.CharField(label="",max_length=10,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date de naissance','id':'naissance'}))
    campus=forms.ModelChoiceField(initial=Campus.objects.first(),queryset=Campus.objects.all(),label="",widget=forms.Select(attrs={'class':'form-control','id':'select_campus'}))
    phone=forms.CharField(label="",required=False,max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Numéro de téléphone','id':'phone'}))

    class Meta():
        model = User
        fields = ['email','username','nom','prenom','password1','password2','promo','majeure','naissance','campus','phone']
        
    def clean_email(self):
        email=self.cleaned_data['email']
        if '@epfedu.fr' not in email:
            raise forms.ValidationError('Entrer votre mail epf')
        try:
            user=User.objects.get(email=email)
            raise forms.ValidationError('Le mail existe déjà')
        except user.DoesNotExist:
            return email
            
        

    def clean_phone(self):
        phone=self.cleaned_data['phone']
        regex=re.compile('^0(6|7)[0-9]{8}$')
        if not regex.match(phone) and phone!="":
            raise forms.ValidationError('Entrer un numéro valide')
        return phone

    def clean_naissance(self):
        naissance=self.cleaned_data['naissance']
        regex=re.compile('^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$')
        if not regex.match(naissance):
            raise forms.ValidationError('Entrer une date valide [dd/mm/YYYY]')
        return naissance

    def save(self,commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["prenom"]
        user.last_name = self.cleaned_data["nom"]
        user.email = self.cleaned_data["email"]
        promo=self.cleaned_data['promo']
        campus=self.cleaned_data['campus']
        phone=self.cleaned_data['phone']
        majeure=self.cleaned_data['majeure']
        naissance=self.cleaned_data['naissance']
        if commit:
            user.save()
            profil=UserProfile(user=user,promo=promo,naissance=naissance,phone=phone,majeure=majeure,campus=campus)
            profil.save()
        return user