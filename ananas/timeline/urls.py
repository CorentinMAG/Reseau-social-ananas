from django.urls import path

from . import views

urlpatterns = [
    path('', views.Timeline.as_view(), name='timeline-home'),
    path('add', views.add_article, name="add-article"),
    path('lire/<int:id>-<slug:slug>', views.lire, name="view_article"),
    path('delete/<int:id>', views.delete_comm, name='delete_comm'),
    path('delete_article/<int:id>', views.delete_article, name='delete-article'),
    path('search/<str:tag>', views.search, name='search'),
    path('<str:type_tag>', views.searchType, name='search-type'),
path(r'^edition/(?P<pk>\d)$', views.ArticleUpdate.as_view(), name='update-article'),
]
