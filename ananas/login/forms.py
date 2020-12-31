from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
from .models import Campus, Master, Student, Administration
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
import re

User = get_user_model()
MAIL = '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9]+)\.([a-z]{2,})$'
REG_MAIL = re.compile(MAIL)

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

        if not REG_MAIL.match(email):
            raise forms.ValidationError('Enter a valid email')
        return email


class Custom_password_reset_form_confirm(SetPasswordForm):
    
    """
    password reset
    """

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}))


class ConnexionForm(forms.Form):
    
    """
    connexion form
    """

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password'}))
    stay_connected = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(
        attrs={'class': 'onoffswitch-checkbox', 'id': 'myonoffswitch'}))

    def clean_email(self):

        email = self.cleaned_data['email']

        if not REG_MAIL.match(email):

            raise forms.ValidationError('Enter a valid email')

        return email


class AutreForm(forms.Form):
    
    """
    Register form
    """

    campus = forms.ModelChoiceField(empty_label=None, queryset=None, label="",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'select_campus_autre'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom.nom@example.fr', 'id': 'autre_email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1_autre'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'id': 'password2_autre'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name', 'id': 'nom_autre'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name', 'id': 'prenom_autre'}))

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['campus'].queryset = Campus.objects.all()

    class Meta:

        model = Administration
        fields = ('first_name', 'last_name', 'password1', 'password2', 'email', 'campus')

    def clean_email(self):
        email = self.cleaned_data['email']

        if not REG_MAIL.match(email):
            raise forms.ValidationError('Enter a valid email')
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError('This email already exist')
        except User.DoesNotExist:
            return email

    def save(self, commit = True):

        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        campus = self.cleaned_data['campus']

        user = User.objects.create_user(
            email = email,
            last_name = last_name, 
            first_name = first_name, 
            password = password, 
            campus = campus,
            is_student = False
        )

        admin = Administration(user = user)
        admin.save()

        if commit:
            user.save()
        return user


class EtudiantForm(UserCreationForm):
    
    """
    Register form for students
    """

    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'john.doe@example.fr', 'id': 'email'}))
    last_name = forms.CharField(label="",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'id': 'nom'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name', 'id': 'prenom'}))
    campus = forms.ModelChoiceField(empty_label=None, queryset=None, label="",
                                    widget=forms.Select(
                                        attrs={'class': 'form-control', 'id': 'select_campus_etudiant'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password1'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Vérification du mot de passe', 'id': 'password2'}))
    master = forms.ModelChoiceField(empty_label=None, queryset=None, label="",
                                     widget=forms.Select(attrs={'class': 'form-control', 'id': 'majeure'}))

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['campus'].queryset = Campus.objects.all()
        self.fields['master'].queryset = Master.objects.all()

    class Meta:

        model = User
        fields = ('master', 'password1', 'password2', 'last_name', 'first_name', 'email', 'campus')

    def clean_email(self):

        email = self.cleaned_data['email']

        if not REG_MAIL.match(email):

            raise forms.ValidationError('Enter a valid email')

        try:

            user = User.objects.get(email=email)
            raise forms.ValidationError('This email already exist')

        except User.DoesNotExist:

            return email

    def save(self, commit=True):

        first_name = self.cleaned_data["first_name"]
        password = self.cleaned_data["password1"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        campus = self.cleaned_data['campus']
        user = User.objects.create_user(
            email = email, 
            last_name = last_name, 
            first_name = first_name, 
            password = password, 
            campus = campus
        )

        master = self.cleaned_data['master']
        student = Student(user=user, master=master)
        student.save()

        if commit:
            user.save()

        return user
