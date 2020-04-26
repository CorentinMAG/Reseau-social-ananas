# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.timeline, name='timeline-home'),
    path('<int:id>', views.lire)
]