from django.http import Http404
from django.shortcuts import render

# Create your views here.
from timeline.models import Article


def timeline(request):
    """
    Afficher tous les articles de notre blog, link à timeline/timeline.html
    """
    # Article.objects.create(titre="Mon troisième article", contenu_post="La dure vie d'un étudiant confiné, tome 3")
    posts = Article.objects.all()
    return render(request, 'timeline/timeline.html', {'posts': posts})


def lire(request, id):
    """
    Permet de lire un post en particulier en fonction de son ID. Accès via timeline/timeline.html
    """
    try:
        post = Article.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'timeline/lire.html', {'post': post})
