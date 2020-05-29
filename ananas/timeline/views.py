from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Article, Commentaires, Tags
from .form import CommentForm, ArticleForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

User = get_user_model()


@login_required
def timeline(request):
    """
    Afficher tous les articles de notre blog, link à timeline/timeline.html
    """
    # Article.objects.create(titre="Mon premier article", contenu_post="La dure vie d'un étudiant confiné, tome 1")
    posts = Article.objects.all()
    print(Tags.objects.get(text_tag='test'))
    args = {'posts': posts}
    return render(request, 'timeline/timeline.html', args)

@login_required
@permission_required('Article.add_article')
def add_article(request):
    """
    Ajoute un nouvel article
    """
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_titre = form.cleaned_data['titre']
            new_auteur = form.cleaned_data['auteur']
            new_photo = form.cleaned_data['photo']
            new_post = form.cleaned_data['contenu_post']
            new_tags = form.cleaned_data['tags']
            print(new_tags, type(new_tags))

            Articl = Article.objects.create(titre=new_titre,
                                            auteur=new_auteur,
                                            contenu_post=new_post,
                                            photo=new_photo)
            Articl.save()
            for tag in new_tags:
                Articl.tags.add(tag)
                Articl.save()
            # Reverse :
            return redirect(reverse('timeline-home'))


        else:
            print('_______________' + 'PAS VALIDE')
            return render(request, 'timeline/add.html')

    else:
        form = ArticleForm()

    args = {'form': form}
    return render(request, 'timeline/add.html', args)


@login_required
def lire(request, id):
    """
    Permet de lire un post en particulier en fonction de son ID. Accès via timeline/timeline.html
    """

    try:
        post = Article.objects.get(id=id)
        comments = Commentaires.objects.filter(id_post=id)
    except post.DoesNotExist:
        raise Http404

    # COMMENTAIRES
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.cleaned_data['contenu_comm']
        truc = request.user
        com = Commentaires.objects.create(contenu_comm=new_comment, id_post=post, id_user=truc)
        com.save()
        comments = Commentaires.objects.filter(id_post=id)  # Actualise liste commentaires

    args = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'timeline/lire.html', args)


@login_required
def search_timeline(request):  # TODO : Chercher selon les tags
    """
    Selectionne les articles correspondant aux champs de recherche
    """
    # Article.objects.create(titre="Mon premier article", contenu_post="La dure vie d'un étudiant confiné, tome 1")
    posts = Article.objects.filter(id_post=id)
    return render(request, 'timeline/timeline.html', {'posts': posts})

# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Article, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'timeline/add_comment_to_post.html', {'form': form})

# class LireView(TemplateView):
#     template_name = "timeline/lire.html"
#
#     def get(self, request):
#         form = CommentForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             your_comment = form.cleaned_data['your_comment']
#             form = CommentForm()
#
#
#         args = {'form': form, 'your_comment': your_comment}
#         return render(request, self.template_name, args)
