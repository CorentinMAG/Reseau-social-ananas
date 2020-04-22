from django.http import Http404
from django.shortcuts import render

# Create your views here.
from timeline.models import Article


def accueil(request):
    return render(request, 'timeline/timeline.html')


def timeline(request):
    """
    Afficher tous les articles de notre blog, link à timeline/timeline.html
    """
    # Article.objects.create(titre="Mon troisième article", contenu_post="La dure vie d'un étudiant confiné, tome 3")
    articles = Article.objects.all()
    return render(request, 'timeline/timeline.html', {'derniers_articles': articles})


def lire(request, id):
    """
    Permet de lire un post en particulier en fonction de son ID. Accès via timeline/timeline.html
    """
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'timeline/lire.html', {'article': article})
