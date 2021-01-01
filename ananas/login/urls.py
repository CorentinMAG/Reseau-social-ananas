from django.urls import path,re_path
from . import views


app_name = 'login'


urlpatterns=[
	path('connexion/', views.connexion, name = 'connexion'),
    path('register/', views.RegisterView, name = "register"),
	path('register/student/', views.StudentView,name = 'student'),
    path('register/admin/', views.AdminView, name = "admin"),
	path('deconnexion/', views.deconnexion, name = 'deconnexion'),
	re_path(r'^password_reset/$', views.MyPasswordResetView.as_view(), name = 'password_reset'),
    re_path(r'^password_reset/done/$', views.MyPasswordResetDoneView.as_view(), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,}-[0-9A-Za-z]{1,})/$',
        views.MyPasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    re_path(r'^reset/done/$', views.MyPasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]+-[0-9A-Za-z]+)/$',
        views.activate, name = 'activate'),
 ]