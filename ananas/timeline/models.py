from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
import os
from django.utils.safestring import mark_safe
from markdown_it import MarkdownIt
from markdown_it.extensions.front_matter import front_matter_plugin
from markdown_it.extensions.footnote import footnote_plugin
from mdeditor.fields import MDTextField


def render_blank_link(self, tokens, idx, options, env):
    aIndex = tokens[idx].attrIndex('target')
    if (aIndex < 0):
        tokens[idx].attrPush(['target', '_blank'])  # add new attribute
    else:
        tokens[idx].attrs[aIndex][1] = '_blank'  # replace value of existing attr

    # pass token to default renderer.
    return self.renderToken(tokens, idx, options, env)


md = (
    MarkdownIt("default")
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .enable('table')
)

md.add_render_rule("link_open", render_blank_link)

User = get_user_model()


class Tags(models.Model):
    """Tag lié à l'article, en facilite sa recherche."""
    text_tag = models.CharField(max_length=50)
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
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de parution")
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu_post = MDTextField()
    tags = models.ManyToManyField(Tags, related_name='tag')
    slug = models.SlugField(max_length=100)
    photo = models.ImageField(upload_to="photos/")
    modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titre

    def get_markdown(self):
        content = self.contenu_post
        markdown_content = md.render(content)
        return mark_safe(markdown_content)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-date"]


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=Article)
def delete_article(sender, instance, **kwargs):
    """Ainsi quand on supprime un article la photo associé est également supprimé
    (inutile de la garder)"""
    if instance.photo:
        _delete_file(instance.photo.path)


class Pieces_jointes_post(models.Model):
    """
    Pièces jointes dans les articles (Photos, documents, ...)
    """
    id_pj = models.AutoField(primary_key=True)
    lien_pj = models.URLField()
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
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_comm = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Date de commentaire", blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def children(self):
        return Commentaires.objects.filter(parent=self)

    def get_markdown(self):
        content = self.contenu_comm
        markdown_content = md.render(content)
        return mark_safe(markdown_content)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        else:
            return True

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


