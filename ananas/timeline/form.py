from django.forms import ModelForm, CharField
from .models import Commentaires, Article
from django import forms
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
    tags = forms.ModelChoiceField(initial=Tags.objects.first(), queryset=Tags.objects.all(), label="",
                                  widget=forms.Select(attrs={'class': 'form-control', 'id': 'tags'}))

    class Meta:
        model = Tags
        fields = ('text_tag',)


# class EtudiantForm(UserCreationForm):
#     """Formulaire d'inscription pour les étudiants"""
#     email = forms.EmailField(label="", widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder': 'prenom.nom@epfedu.fr', 'id': 'email'}))
#     nom = forms.CharField(label="",
#                           widget=forms.TextInput(
#                               attrs={'class': 'form-control', 'placeholder': 'Nom', 'id': 'nom'}))
#     prenom = forms.CharField(label="", widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Prénom', 'id': 'prenom'}))
#     campus = forms.ModelChoiceField(initial=Campus.objects.first(), queryset=Campus.objects.all(), label="",
#                                     widget=forms.Select(
#                                         attrs={'class': 'form-control', 'id': 'select_campus_etudiant'}))
#     password1 = forms.CharField(label="", widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Mot de passe', 'id': 'password1'}))
#     password2 = forms.CharField(label="", widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Vérification du mot de passe', 'id': 'password2'}))
#     majeure = forms.ModelChoiceField(initial=Majeure.objects.first(), queryset=Majeure.objects.all(), label="",
#                                      widget=forms.Select(attrs={'class': 'form-control', 'id': 'majeure'}))
#
#     class Meta:
#         model = User
#         fields = ('majeure', 'password1', 'password2', 'nom', 'prenom', 'email', 'campus')
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if '@epfedu.fr' not in email:
#             raise forms.ValidationError('Entrer votre mail epf')
#         try:
#             user = User.objects.get(email=email)
#             raise forms.ValidationError('Le mail existe déjà')
#         except User.DoesNotExist:
#             return email
#
#     def save(self, commit=True):
#         prenom = self.cleaned_data["prenom"]
#         password = self.cleaned_data["password1"]
#         nom = self.cleaned_data["nom"]
#         email = self.cleaned_data["email"]
#         campus = self.cleaned_data['campus']
#         user = User.objects.create_user(email=email, last_name=nom, first_name=prenom, password=password,
#                                         campus=campus)
#         user.is_active = False
#
#         majeure = self.cleaned_data['majeure']
#         profilEtudiant = Etudiant(user=user, majeure=majeure)
#         profilEtudiant.save()
#         if commit:
#             user.save()
#         return user


class ArticleForm(forms.ModelForm):
    titre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre', 'id': 'titre_article'}))
    contenu_post = forms.CharField(widget=PagedownWidget)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'form-control', 'id': 'tags_article'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'id': 'file_article'}))

    class Meta:
        model = Article
        exclude = ('auteur',)

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
