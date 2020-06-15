import datetime

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from .models import Article, Commentaires, Tags
from .form import CommentForm, ArticleForm, AddTags, SearchTag
from django.contrib.auth.decorators import login_required, permission_required
import json
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class Timeline(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'posts'
    template_name = 'timeline/timeline.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(Timeline, self).get_context_data(**kwargs)

        context['username'] = mark_safe(json.dumps(self.request.user.first_name))
        context['tags'] = Tags.objects.exclude(text_tag='Tous les tags')
        context['email'] = mark_safe(json.dumps(self.request.user.email))
        context['formTri'] = SearchTag()
        context['can_add_article'] = self.request.user.has_perm('timeline.add_article')
        return context

    def post(self, request, *args, **kwargs):
        formTri = SearchTag(request.POST)
        if formTri.is_valid():
            tag_value = formTri['text_tag'].value()
            return search(request, tag_value)


def search(request, tag):
    """
    recherche en fonction d'un tag ==> Go timeline filtrée
    """
    tags = Tags.objects.exclude(text_tag='Tous les tags')
    posts = Article.objects.filter(tags__text_tag=tag)
    can_add_article = request.user.has_perm('timeline.add_article')
    formTri = SearchTag()
    args = {'posts': posts,
            'can_add_article': can_add_article,
            'formTri': formTri,
            'tags': tags,
            'article': True,
            'username': mark_safe(json.dumps(request.user.first_name)),
            'email': mark_safe(json.dumps(request.user.email))
            }
    return render(request, 'timeline/timeline.html', args)


def searchType(request, type_tag):
    """
    recherche en fonction d'un tag ==> Go timeline filtrée
    """
    formTri = SearchTag()
    posts = Article.objects.filter(tags__type_tag=type_tag).distinct()

    tags = Tags.objects.exclude(text_tag='Tous les tags')

    can_add_article = request.user.has_perm('timeline.add_article')
    args = {'posts': posts,
            'can_add_article': can_add_article,
            'formTri': formTri,
            'tags': tags,
            'article': True,
            'username': mark_safe(json.dumps(request.user.first_name)),
            'email': mark_safe(json.dumps(request.user.email))
            }
    if request.method == 'POST':
        formTri = SearchTag(request.POST)
        if formTri.is_valid():
            tag_value = formTri['text_tag'].value()
            return search(request, tag_value)
    return render(request, 'timeline/timeline.html', args)


def delete_article(request, id):
    article = Article.objects.get(pk=id)
    if article.auteur == request.user or request.user.is_superuser:
        article.delete()
    return redirect(reverse('timeline-home'))


@login_required
def delete_comm(request, id):
    comm = Commentaires.objects.get(pk=id)
    article = comm.id_post.pk
    slug = comm.id_post.slug
    if comm.id_user == request.user:
        comm.delete()
    return redirect(reverse('view_article', kwargs={'id': article, 'slug': slug}))

@login_required
@permission_required('timeline.add_article')
def add_article(request):
    """
    Ajoute un nouvel article
    """
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        formTag = AddTags(request.POST)
        if form.is_valid():
            new_titre = form.cleaned_data['titre']
            new_auteur = request.user
            new_photo = form.cleaned_data['photo']
            new_post = form.cleaned_data['contenu_post']
            new_tags = form.cleaned_data['tags']

            new_article = Article.objects.create(titre=new_titre,
                                                 auteur=new_auteur,
                                                 contenu_post=new_post,
                                                 photo=new_photo,
                                                 slug=slugify(new_titre))
            new_article.save()
            for tag in new_tags:
                new_article.tags.add(tag)
                new_article.save()
            return redirect(reverse('timeline-home'))
        elif formTag.is_valid():
            new_tag_text = formTag.cleaned_data['text_tag']
            new_type_tag = formTag.cleaned_data['type_tag']
            new_tag = Tags.objects.create(type_tag=new_type_tag, text_tag=new_tag_text)
            new_tag.save()
            return redirect(reverse('add-article'))
        else:
            return render(request, 'timeline/add.html')

    else:
        form = ArticleForm()
        formTag = AddTags()
    args = {'form': form, 'can_add_tag': request.user.has_perm('timeline.add_tags'), 'formTag': formTag}
    return render(request, 'timeline/add.html', args)


@login_required
def lire(request, id, slug):
    """
    Permet de lire un post en particulier en fonction de son ID. Accès via timeline/timeline.html
    """

    tags = Tags.objects.exclude(text_tag='Tous les tags')
    formTri = SearchTag()
    post = Article.objects.get(id=id, slug=slug)
    tagsArticle = post.tags.all()
    comments = Commentaires.objects.filter(id_post=id, parent=None)

    # COMMENTAIRES
    if request.method == 'POST':
        form = CommentForm(request.POST)
        formTri = SearchTag(request.POST)
        if formTri.is_valid():
            tag_value = formTri['text_tag'].value()
            return search(request, tag_value)

        if form.is_valid():
            new_comment = form.cleaned_data['contenu_comm']
            truc = request.user
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_qs = Commentaires.objects.filter(pk=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()
            com = Commentaires.objects.create(contenu_comm=new_comment, id_post=post, id_user=truc, parent=parent_obj)
            com.save()
            comments = Commentaires.objects.filter(id_post=id, parent=None)  # Actualise liste commentaires
            form = CommentForm()
    else:
        form = CommentForm()

    args = {'post': post, 'comments': comments, 'form': form, 'tags': tags, 'tagsArticle': tagsArticle,
            'formTri': formTri,
            'username': mark_safe(json.dumps(request.user.first_name)),
            'email': mark_safe(json.dumps(request.user.email)), 'article': True}
    return render(request, 'timeline/lire.html', args)


class ArticleUpdate(LoginRequiredMixin,UpdateView):
    model = Article
    template_name = 'timeline/add.html'
    form_class = ArticleForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['photo'].required = None
        return form

    def form_valid(self, form):
        self.object.modified = datetime.datetime.now()
        self.object.save()
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse_lazy(lire, kwargs={'id': self.object.pk, 'slug': self.object.slug})

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['id'], slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdate, self).get_context_data(**kwargs)

        obj = super(ArticleUpdate, self).get_object()
        context['file'] = obj.photo.url
        return context
