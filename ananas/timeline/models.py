from django.utils import timezone
from django.db import models

# Create your models here.



class Article(models.Model):
    """
    Articles postés sur la timeline
    """
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=42)
    contenu_post = models.TextField(null=True)
    photo = models.ImageField(upload_to="photos")
    date = models.DateTimeField(default=timezone.now,
                               verbose_name="Date de parution")

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Article"
