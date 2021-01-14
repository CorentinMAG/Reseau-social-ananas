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

    """
    link inside an article are opened in a new window 
    (we don't leave the current page)
    """

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

    """
    Article's tags
    """

    text_tag = models.CharField(max_length = 50)
    type_tag = models.CharField(max_length = 50)

    def __str__(self):
        return self.text_tag

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Article(models.Model):
    
    """
    Article
    """

    date = models.DateTimeField(auto_now_add = True, verbose_name = "publish date")
    title = models.CharField(max_length = 100)
    publisher = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_articles')
    post = MDTextField()
    tags = models.ManyToManyField(Tags, blank = True)
    slug = models.SlugField(max_length = 100)
    photo = models.ImageField(upload_to = "article/")
    modified = models.DateTimeField(null = True)

    def __str__(self):
        return self.title

    def get_markdown(self):
        content = self.post
        markdown_content = md.render(content)
        return mark_safe(markdown_content)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-date"]


class Comment(models.Model):

    """
    Article's comments
    """

    content = models.CharField(max_length = 500)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_comments')
    date = models.DateTimeField(auto_now_add = True, verbose_name = "comment date")
    parent = models.ForeignKey('self', null = True, blank = True, on_delete = models.CASCADE)

    def children(self):
        return Comment.objects.filter(parent = self)

    def get_markdown(self):
        content = self.content
        markdown_content = md.render(content)
        return mark_safe(markdown_content)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        else:
            return True

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-date"]


@receiver(post_delete, sender = Article)
def delete_article(sender, instance, **kwargs):

    """
    delete photo from the file system when an Article is deleted
    """

    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)