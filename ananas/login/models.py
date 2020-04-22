from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .Manager import CustomUserManager


class Campus(models.Model):
    nom = models.CharField(max_length=30, unique=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.nom


class Majeure(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Majeures"

    def __str__(self):
        return self.nom


# Le model utilisateur de base qu'on va utiliser à la place
# du model User prédéfini de django
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/')
    is_etudiant = models.BooleanField(default=True, verbose_name="Etudiant")
    is_autre = models.BooleanField(default=False, verbose_name="Autre")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Etudiant(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_etudiant", on_delete=models.CASCADE)
    promo = models.IntegerField()
    majeure = models.ForeignKey(Majeure, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Administration(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_admin", on_delete=models.CASCADE)
    poste = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
