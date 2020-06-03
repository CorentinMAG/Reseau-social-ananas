from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .forms import ProfilForm
from login.models import Etudiant
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, reverse, redirect

User = get_user_model()


@login_required
def profil(request, email):
    user = get_object_or_404(User, email=email)
    args = {
        'UserProfile': user
    }
    return render(request, 'profil/profil.html', args)


@login_required
def redirectToProfil(request):
    user = request.user
    return redirect(reverse('profile-home', kwargs={'email': user.email}))


def _userdata(user):
    initial_data = {
        'prenom': user.first_name,
        'nom': user.last_name,
        'campus': user.campus,
        'email': user.email,
        'naissance': user.Birthdate,
        'avatar': user.avatar
    }
    if user.is_autre:
        initial_data['poste'] = user.user_admin.poste
    elif user.is_etudiant and user.is_superuser == False:
        initial_data['majeure'] = user.user_etudiant.majeure
    return initial_data


@login_required
def profilEdit(request):
    """
    Profil de l'utilisateur.
    """

    """Vue qui se charge d'afficher le formulaire
    d'inscription pour les étudiants"""
    user = request.user

    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            if user.is_autre:
                photo = form.cleaned_data['photo']
                first_name = form.cleaned_data['prenom']
                last_name = form.cleaned_data['nom']
                birthdate = form.cleaned_data['naissance']
                if photo is not None:
                    user.photo = photo
                if first_name != user.first_name:
                    user.first_name = first_name
                if last_name != user.last_name:
                    user.last_name = last_name
                if birthdate != "":
                    user.Birthdate = birthdate
                poste = form.cleaned_data['poste']
                if poste != "":
                    user.user_admin.poste = poste
                    user.user_admin.save()
                if form.cleaned_data['campus'] != user.campus:
                    user.campus = form.cleaned_data['campus']
                user.save()
            else:
                photo = form.cleaned_data['photo']
                first_name = form.cleaned_data['prenom']
                last_name = form.cleaned_data['nom']
                birthdate = form.cleaned_data['naissance']
                if photo is not None:
                    user.photo = photo
                if first_name != user.first_name:
                    user.first_name = first_name
                if last_name != user.last_name:
                    user.last_name = last_name
                if birthdate != "":
                    user.Birthdate = birthdate
                if user.is_superuser:
                    try:
                        user.user_etudiant
                    except:
                        etudiant = Etudiant(user=user,majeure=None)
                        etudiant.save()
                print(form.cleaned_data['majeure'])
                print(user.user_etudiant.majeure)
                if form.cleaned_data['majeure'] != user.user_etudiant.majeure:

                    user.user_etudiant.majeure = form.cleaned_data['majeure']
                    user.user_etudiant.save()
                if form.cleaned_data['campus'] != user.campus:
                    user.campus = form.cleaned_data['campus']
                user.save()

            return redirect(reverse('profile-home', kwargs={'email': user.email}))
    else:
        initial_data = _userdata(user)
        form = ProfilForm(initial_data)
    args = {'form': form, 'UserProfile': user}
    return render(request, 'profil/profiledit.html', args)
