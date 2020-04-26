from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .Manager import CustomUserManager


class Campus(models.Model):
    """"Recense les différents campus de l'école"""
    nom = models.CharField(max_length=30, unique=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.nom


class Majeure(models.Model):
    """Recense les différentes majeures de l'école, ainsi
    que les niveaux 1A,2A et 3A"""
    nom = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Majeures"

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    """modèle propre aux étudiant,
    relié au modèle CustomUser avec lequel il partage les attributs"""
    user = models.OneToOneField(CustomUser, related_name="user_etudiant", on_delete=models.CASCADE)
    promo = models.IntegerField()
    majeure = models.ForeignKey(Majeure, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class CustomUser(AbstractUser):
    """Le model utilisateur qu'on va utiliser à la place
    du model User de base (on ne veut pas de champ username)"""
    username = None
    GENDER = (
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    )
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Prénom')
    last_name = models.CharField(max_length=50, verbose_name='Nom')
    is_etudiant = models.BooleanField(default=True, verbose_name="Etudiant")
    is_autre = models.BooleanField(default=False, verbose_name="Autre")
    genre = models.CharField(choices=GENDER, default='homme', max_length=5)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Etudiant(models.Model):
    """modèle propre aux étudiant,
    relié au modèle CustomUser avec lequel il partage les attributs"""
    user = models.OneToOneField(CustomUser, related_name="user_etudiant", on_delete=models.CASCADE)
    promo = models.IntegerField()
    avatar = models.ImageField(upload_to='avatar/',blank=True)
    phone = PhoneNumberField(blank=True, verbose_name='numéro de téléphone')
    Birthdate = models.CharField(max_length=10, verbose_name='Date de naissance',blank=True)
    majeure = models.ForeignKey(Majeure, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Administration(models.Model):
    """modèle propre à l'administration,
    relié au modèle CustomUser avec lequel il partage les attributs"""
    user = models.OneToOneField(CustomUser, related_name="user_admin", on_delete=models.CASCADE)
    poste = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatar/',blank=True)
    phone = PhoneNumberField(blank=True, verbose_name='numéro de téléphone')
    Birthdate = models.CharField(max_length=10, verbose_name='Date de naissance',blank=True)
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
