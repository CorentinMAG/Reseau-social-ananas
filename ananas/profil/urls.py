# chat/urls.py
from django.http import HttpResponseRedirect
from django.urls import path

from . import views

urlpatterns = [
    path('<str:email>', views.profil, name='profile-home'),
    path('',views.redirectToProfil),
    path('update/',views.profilEdit,name="update-profil")
]