from django.contrib import admin
from django.urls import path,include,re_path
from django.http import HttpResponseRedirect
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

handler404 = 'login.views.error_404'
handler500 = 'login.views.error_500'
handler403 = 'login.views.error_403'

urlpatterns = [

	# we have changed a bit Envs/django/Lib/site-packages/django/contrib/admin/templates/admin/base.html
	# file in order to directly be redirected to account/connexion when logout the admin site
	# one other way to do that is to create another path(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'})
	# but as we have already done a generic import of all auth urls it is not convenient 
    path('admin/', admin.site.urls),
    path('account/', include('login.urls', namespace = 'login')),
    path('messenger-api/', include('messenger.api.urls')),
    path('messenger/', include('messenger.urls')),
    path('timeline/', include("timeline.urls", namespace = 'timeline')),
    path('profil/', include("profil.urls", namespace = 'profil')),
    path('mdeditor/', include('mdeditor.urls')),
	path('', include('pagedown.urls')),
    path('', lambda r: HttpResponseRedirect('account/connexion')),
    path('activity/', include('actstream.urls')),
    path('__debug__/', include(debug_toolbar.urls))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
