from django.urls import path

from . import views

app_name = 'profil'

urlpatterns = [
    path('<str:email>', views.profil, name = 'profil'),
    path('update/', views.profilEdit, name = "update")
]