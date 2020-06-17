"""ananas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponseRedirect
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'login.views.error_404'
handler500 = 'login.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('login.urls')),
    path('messenger-api/',include('messenger.api.urls')),
    path('messenger/',include('messenger.urls')),
    path('timeline/', include("timeline.urls")),
    path('profil/', include("profil.urls")),
    path('mdeditor/', include('mdeditor.urls')),
path('', include('pagedown.urls')),
    path('',lambda r: HttpResponseRedirect('account/connexion')),
    path('activity/', include('actstream.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


