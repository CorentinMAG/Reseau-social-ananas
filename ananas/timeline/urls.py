from django.urls import path

from . import views


app_name = 'timeline'

urlpatterns = [
    path('', views.Home.as_view(), name = 'timeline-home'),
    path('add', views.CreateArticle.as_view(), name = "add_article"),
    path('lire/<int:pk>-<slug:slug>', views.viewArticle, name = "view_article"),
    path('delete/<int:pk>', views.delete_comm, name='delete_comm'),
    path('delete_article/<int:pk>', views.delete_article, name = 'delete_article'),
    #path('search/<str:tag>', views.search, name = 'search'),
    #path('<str:type_tag>', views.searchType, name = 'search-type'),
    path('edition/<int:pk>-<slug:slug>', views.ArticleUpdate.as_view(), name = 'update_article'),
]
