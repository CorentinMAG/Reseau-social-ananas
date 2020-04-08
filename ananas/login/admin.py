from django.contrib import admin
from .models import UserProfile,Majeures,Campus

admin.site.register(Majeures)
admin.site.register(Campus)
admin.site.register(UserProfile)
