from django.urls import path,re_path
from . import views


urlpatterns=[
	path('connexion/',views.connexion,name='connexion'),
	path('register/',views.RegisterView.as_view(),name='register'),
	path('deconnexion/',views.deconnexion,name='deconnexion'),
	path('redirection/',views.view_redirection,name='redirection'),
	re_path(r'^password_reset/$', views.MyPasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password_reset/done/$', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('error/forbidden',views.Forbidden.as_view(),name='forbidden')
	
]