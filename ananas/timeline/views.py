import datetime

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from .models import Article, Comment, Tags
from .form import CommentForm, ArticleForm, AddTags, SearchTag
from django.contrib.auth.decorators import login_required, permission_required
import json
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from actstream import action

User = get_user_model()


class Home(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'timeline/timeline.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        #context['tags'] = Tags.objects.all()
        #context['formTri'] = SearchTag()
        return context

    # def post(self, request, *args, **kwargs):
    #     formTri = SearchTag(request.POST)
    #     if formTri.is_valid():
    #         tag_value = formTri['text_tag'].value()
    #         return search(request, tag_value)


# def search(request, tag):
#     """
#     recherche en fonction d'un tag ==> Go timeline filtrée
#     """
#     tags = Tags.objects.exclude(text_tag = 'Tous les tags')
#     posts = Article.objects.filter(tags__text_tag = tag)
#     can_add_article = request.user.has_perm('timeline.add_article')
#     formTri = SearchTag()
#     args = {'posts': posts,
#             'can_add_article': can_add_article,
#             'formTri': formTri,
#             'tags': tags,
#             'article': True,
#             'username': mark_safe(json.dumps(request.user.first_name)),
#             'email': mark_safe(json.dumps(request.user.email))
#             }
#     return render(request, 'timeline/timeline.html', args)


# def searchType(request, type_tag):
#     """
#     recherche en fonction d'un tag ==> Go timeline filtrée
#     """
#     formTri = SearchTag()
#     posts = Article.objects.filter(tags__type_tag = type_tag).distinct()

#     tags = Tags.objects.exclude(text_tag='Tous les tags')

#     can_add_article = request.user.has_perm('timeline.add_article')
#     args = {'posts': posts,
#             'can_add_article': can_add_article,
#             'formTri': formTri,
#             'tags': tags,
#             'article': True,
#             'username': mark_safe(json.dumps(request.user.first_name)),
#             'email': mark_safe(json.dumps(request.user.email))
#             }
#     if request.method == 'POST':
#         formTri = SearchTag(request.POST)
#         if formTri.is_valid():
#             tag_value = formTri['text_tag'].value()
#             return search(request, tag_value)
#     return render(request, 'timeline/timeline.html', args)

@login_required
def delete_article(request, pk):
    article = Article.objects.get(pk = pk)
    if article.publisher == request.user or request.user.is_superuser:
        article.delete()
    return redirect('timeline:timeline-home')


@login_required
def delete_comm(request, pk):
    comm = Comment.objects.get(pk = pk)
    article = comm.id_post.pk
    slug = comm.id_post.slug
    if comm.id_user == request.user:
        comm.delete()
    return redirect('timeline:view_article', kwargs={'pk': article, 'slug': slug})


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

            new_article = Article.objects.create(title = new_titre,
                                                 publisher = new_auteur,
                                                 post = new_post,
                                                 photo = new_photo,
                                                 slug = slugify(new_titre))
            for tag in new_tags:
                new_article.tags.add(tag)
            action.send(request.user, verb = "article creation", action_object = new_article)
            return redirect(reverse('timeline-home'))
        elif formTag.is_valid():
            new_tag_text = formTag.cleaned_data['text_tag']
            new_type_tag = formTag.cleaned_data['type_tag']
            new_tag = Tags.objects.create(type_tag = new_type_tag, text_tag = new_tag_text)
            new_tag.save()
            return redirect('timeline:add-article')
        else:
            return render(request, 'timeline/add.html')

    else:
        form = ArticleForm()
        formTag = AddTags()
    args = {'form': form, 'can_add_tag': request.user.has_perm('timeline.add_tags'), 'formTag': formTag}
    return render(request, 'timeline/add.html', args)


class CreateArticle(CreateView):
    success_url = '/'
    form_class = ArticleForm
    template_name = 'timeline/add.html'


@login_required
def viewArticle(request, pk, slug):
    """
    Permet de lire un post en particulier en fonction de son ID. Accès via timeline/timeline.html
    """

    tags = Tags.objects.exclude(text_tag = 'Tous les tags')
    formTri = SearchTag()
    article = Article.objects.get(pk = pk, slug = slug)
    tagsArticle = article.tags.all()
    comments = Comment.objects.filter(article = pk, parent = None)

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
                parent_qs = Comment.objects.filter(pk = parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()
            com = Comment.objects.create(content = new_comment, article = post, user = truc, parent = parent_obj)
            com.save()
            action.send(request.user, verb = "comment creation", action_object = com)
            comments = Comments.objects.filter(article = pk, parent = None)  # Actualise liste commentaires
            form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'article': article, 
        'comments': comments, 
        'form': form, 
        'tags': tags, 
        'tagsArticle': tagsArticle,
        'formTri': formTri,
        'username': mark_safe(json.dumps(request.user.first_name)),
        'email': mark_safe(json.dumps(request.user.email)),
    }

    return render(request, 'timeline/lire.html', context)

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'timeline/add.html'
    form_class = ArticleForm

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['photo'].required = None
        return form

    def form_valid(self, form):
        self.object.modified = datetime.datetime.now()
        self.object.save()
        self.object = form.save()
        action.send(self.request.user, verb = "article updated", action_object = self.object)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(lire, kwargs = {'pk': self.object.pk, 'slug': self.object.slug})

    def get_queryset(self):
        return Article.objects.filter(pk = self.kwargs['pk'], slug = self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdate, self).get_context_data(**kwargs)

        obj = super(ArticleUpdate, self).get_object()
        context['file'] = obj.photo.url
        return context
