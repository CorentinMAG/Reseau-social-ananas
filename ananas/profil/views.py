from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .forms import UpdateAdminProfil, UpdateUserProfil, UpdateStudentProfil
from login.models import Student
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, reverse, redirect
from timeline.models import Article, Comment
from messenger.models import Message
from actstream import action
from actstream.models import user_stream

User = get_user_model()


@login_required
def profil(request, email):

    """
    user profil
    """

    user = get_object_or_404(User, email = email)

    args = {
        'UserProfil': user,
        'countMessages': Message.objects.filter(contact = user).count(),
        'countArticles': Article.objects.filter(publisher = user).count(),
        'countComments': Comment.objects.filter(user = user).count()
    }
    
    return render(request, 'profil/profil.html', args)


@login_required
def profilEdit(request):

    """
    update user profil
    """

    user = request.user

    if request.method == 'POST':


        user_form = UpdateUserProfil(request.POST, request.FILES, instance = user)

        if user.is_student:
            child_form = UpdateStudentProfil(request.POST, instance = user.user_student)
        else:
            child_form = UpdateAdminProfil(request.POST, instance = user.user_admin)


        if all((user_form.is_valid(), child_form.is_valid())):


            new_child_data = child_form.save()
            new_user_data = user_form.save()

            action.send(request.user, verb = 'profil updated')

            return redirect(reverse('profil:profil',kwargs = {'email':user.email}))
    else:

        user_form = UpdateUserProfil(instance = user)

        if user.is_student:
            child_form = UpdateStudentProfil(instance = user.user_student)
        else:
            child_form = UpdateAdminProfil(instance = user.user_admin)

        args = {
            'user_form': user_form,
            'child_form':child_form,
            'UserProfil': user,
            'countMessages': Message.objects.filter(contact = user).count(),
            'countArticles': Article.objects.filter(publisher = user).count(),
            'countCommentaires': Comment.objects.filter(user = user).count()
        }

    return render(request, 'profil/profiledit.html', args)
