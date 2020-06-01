# chat/urls.py
from django.urls import path

from . import views
#from .views import LireView

urlpatterns = [
    path('', views.timeline, name='timeline-home'),
    path('add', views.add_article,name="add-article"),
    path('<int:id>', views.lire,name="view_article"),
    path('delete/<int:id>',views.delete_comm,name='delete_comm'),
    path('add_tag',views.add_tag,name="add-tag")
    #path('<int:id>', LireView.as_view(), name='timeline-lire')
]
