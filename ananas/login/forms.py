from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import UserProfile,Campus,Majeures

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
    promo=forms.IntegerField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Promo','id':'promo'}))
    majeure=forms.ModelChoiceField(initial=Majeures.objects.get(nom='Majeure aéronautique & espace'),queryset=Majeures.objects.all(),label="",widget=forms.Select(attrs={'class':'form-control','id':'majeure'}))
    naissance=forms.CharField(label="",widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date de naissance','id':'naissance'}))
    campus=forms.ModelChoiceField(initial=Campus.objects.get(nom='Sceaux'),queryset=Campus.objects.all(),label="",widget=forms.Select(attrs={'class':'form-control','id':'select_campus'}))
    phone=forms.IntegerField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Numéro de téléphone','id':'phone'}))

    class Meta():
        model = User
        fields = ['email','username','nom','prenom','password1','password2','promo','majeure','naissance','campus','phone']
        
    def clean_email(self):
        email=self.cleaned_data['email']
        if '@epfedu.fr' not in email:
            raise forms.ValidationError('Entrer votre mail epf')
        return email

    def clean_phone(self):
        phone=self.cleaned_data['phone']
        if len(str(phone))!=9:
            raise forms.ValidationError('Entrer un numéro valide')
        return phone

    def save(self,commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["nom"]
        user.last_name = self.cleaned_data["prenom"]
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