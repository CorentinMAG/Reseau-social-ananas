from django.shortcuts import render

# Create your views here.


def profil(request):
    """
    Profil de l'utilisateur.
    """
    #Article.objects.create(titre="Mon premier article", contenu_post="La dure vie d'un étudiant confiné, tome 1")
    args = {'user': request.user}
    print(type(args['user']))
    return render(request, 'profil/profil.html', args)