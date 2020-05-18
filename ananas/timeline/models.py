from django.db.models import DateField
from django.utils import timezone
from django.db import models


class Tags(models.Model):
    """Tag lié à l'article, en facilite sa recherche."""
    id_tag = models.AutoField(primary_key=True)
    text_tag = models.CharField(max_length=100)
    type_tag = models.CharField(max_length=50)

    def __str__(self):
        return self.text_tag

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Article(models.Model):
    """
    Un post posté sur la timeline
    """
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu_post = models.TextField(null=True)
    tags = models.ManyToManyField(Tags)

    photo = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.titre

    class Meta:
        # Change l'affichage du nom dans l'interface admin
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-date"]


class Tags_article(models.Model):
    """Liaison 1-n entre article et tags"""
    id_tag_article = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Pieces_jointes_post(models.Model):
    """
    Pièces jointes dans les articles (Photos, documents, ...)
    """
    id_pj = models.AutoField(primary_key=True)
    lien_pj = models.URLField()
    # type_pj = titre_post = models.CharField(max_length=30)
    id_post = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.lien_pj


class Commentaires(models.Model):
    """
    Commentaires du post.
    """
    id_comm = models.AutoField(primary_key=True)
    contenu_comm = models.CharField(max_length=500)
    id_post = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)
    # id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_comm = models.DateTimeField(auto_now=True,
                                     verbose_name="Date de commentaire", blank=True, null=True)
    last_modif_comm = models.DateTimeField(auto_now=True,
                                           verbose_name="Date dernière modification", blank=True, null=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.contenu_comm

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = "Commentaires"
        ordering = ["-date_comm"]


class Likes(models.Model):
    """
    Likes posés par un User sur un post
    """
    id_like = models.AutoField(primary_key=True)
    id_post = models.ForeignKey(Article, on_delete=models.CASCADE)
    # id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_like = models.DateTimeField()

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = "Likes"


class Pieces_jointes_comm(models.Model):
    """
    Pièces jointes dans les comms
    """
    id_pj = models.AutoField(primary_key=True)
    # lien_pj = models.URLField()
    # type_pj = models.CharField(max_length=30)
    id_comm = models.ForeignKey(Commentaires, on_delete=models.CASCADE)

    def __str__(self):
        return self.lien_pj
