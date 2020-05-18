# chat/urls.py
from django.urls import path

from . import views
#from .views import LireView

urlpatterns = [
    path('', views.timeline, name='timeline-home'),
    path('<int:id>', views.lire),
    #path('<int:id>', LireView.as_view(), name='timeline-lire')
]