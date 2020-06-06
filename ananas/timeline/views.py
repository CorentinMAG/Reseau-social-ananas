from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from .models import Article, Commentaires, Tags
from .form import CommentForm, ArticleForm, AddTags, SearchTag
from django.contrib.auth.decorators import login_required, permission_required
import json
from django.utils.safestring import mark_safe
from django.utils.text import slugify

User = get_user_model()


@login_required
def timeline(request):
    """
    Afficher tous les articles de notre blog, link à timeline/timeline.html
    """
    # Article.objects.create(titre="Mon premier article", contenu_post="La dure vie d'un étudiant confiné, tome 1")
    tags = Tags.objects.exclude(text_tag='All').order_by('text_tag')[:6]
    form = SearchTag()
    if request.method == 'GET':
        posts = Article.objects.all()
        can_add_article = request.user.has_perm('timeline.add_article')
        args = {'posts': posts, 'form': form, 'can_add_article': can_add_article,
                'username': mark_safe(json.dumps(request.user.first_name)),
                'tags':tags,
                'email': mark_safe(json.dumps(request.user.email))}
        return render(request, 'timeline/timeline.html', args)
    elif request.method == 'POST':
        form = SearchTag(request.POST)
        id_tag_search = int(form['text_tag'].value())
        return search(request, id_tag_search)


def search(request, int):
    """
    recherche en fonction d'un tag ==> Go timeline filtrée
    """
    tag = Tags.objects.get(pk=int)
    tags = Tags.objects.exclude(text_tag='All').order_by('text_tag')[:6]
    if tag.text_tag == 'All':
        posts = Article.objects.all()
    else:
        posts = Article.objects.filter(tags=int)
    can_add_article = request.user.has_perm('timeline.add_article')
    form = SearchTag()
    args = {'posts': posts,
            'can_add_article': can_add_article,
            'form': form,
            'tags':tags,
            'username': mark_safe(json.dumps(request.user.first_name)),
            'email': mark_safe(json.dumps(request.user.email))
            }
    return render(request, 'timeline/timeline.html', args)


def delete_article(request, id):
    article = Article.objects.get(pk=id)
    if article.auteur == request.user:
        article.delete()
    return redirect(reverse('timeline-home'))


@login_required
def delete_comm(request, id):
    comm = Commentaires.objects.get(pk=id)
    article = comm.id_post.pk
    if comm.id_user == request.user:
        comm.delete()
    return redirect(reverse('view_article', kwargs={'id': article}))


@login_required
@permission_required('timeline.add_tags')
def add_tag(request):
    if request.method == 'POST':
        form = AddTags(request.POST)
        if form.is_valid():
            new_tag_text = form.cleaned_data['text_tag']
            new_type_tag = form.cleaned_data['type_tag']
            new_tag = Tags.objects.create(type_tag=new_type_tag, text_tag=new_tag_text)
            new_tag.save()
            return redirect(reverse('add-article'))
        else:
            return render(request, 'timeline/addTag.html')
    else:
        form = AddTags()
        return render(request, 'timeline/addTag.html', {'form': form})


@login_required
@permission_required('timeline.add_article')
def add_article(request):
    """
    Ajoute un nouvel article
    """
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
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
        else:
            return render(request, 'timeline/add.html')

    else:
        form = ArticleForm()
    args = {'form': form, 'can_add_tag': request.user.has_perm('timeline.add_tags')}
    return render(request, 'timeline/add.html', args)


@login_required
def lire(request, id, slug):
    """
    Permet de lire un post en particulier en fonction de son ID. Accès via timeline/timeline.html
    """

    tags = Tags.objects.exclude(text_tag='All').order_by('text_tag')[:6]
    try:
        post = Article.objects.get(id=id, slug=slug)
        tagsArticle = post.tags.all()
        comments = Commentaires.objects.filter(id_post=id)
    except post.DoesNotExist:
        raise Http404

    # COMMENTAIRES
    form = CommentForm(request.POST)
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

    args = {'post': post, 'comments': comments, 'form': form,'tags':tags ,'tagsArticle': tagsArticle,
            'username': mark_safe(json.dumps(request.user.first_name)),
            'email': mark_safe(json.dumps(request.user.email)), 'article': True}
    return render(request, 'timeline/lire.html', args)
