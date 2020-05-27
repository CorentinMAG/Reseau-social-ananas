from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .forms import ProfilForm
from login.models import Etudiant


@login_required
def profil(request):
    """
    Profil de l'utilisateur.
    """

    """Vue qui se charge d'afficher le formulaire
    d'inscription pour les étudiants"""
    if request.method == 'POST':
        form = profilForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

    else:
        etudiant = Etudiant.objects.get(user_id=request.user.email)
        initial_data = {
            'prenom': request.user.first_name,
            'nom': request.user.last_name,
            'majeure': etudiant.majeure_id,
            'campus': etudiant.campus_id,
            'email': request.user.email,
            'naissance': etudiant.Birthdate,
            'avatar': request.user.avatar
        }
        form = ProfilForm(initial_data)

        args = {'user': request.user, 'form': form}

        print(type(args['user']))
        return render(request, 'profil/profil.html', args)
