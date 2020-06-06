from django.urls import path

from . import views

urlpatterns = [
    path('', views.timeline, name='timeline-home'),
    path('add', views.add_article, name="add-article"),
    path('<int:id>-<slug:slug>', views.lire, name="view_article"),
    path('delete/<int:id>', views.delete_comm, name='delete_comm'),
    path('add_tag', views.add_tag, name="add-tag"),
    path('delete_article/<int:id>', views.delete_article, name='delete-article'),
    path('search/<int:int>', views.search, name='search'),
    path('searchtype/<str:type_tag>', views.searchType, name='search-type'),
]
