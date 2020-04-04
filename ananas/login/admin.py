from django.contrib import admin
from .models import UserProfile,Majeures,Campus
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(UserProfile)
admin.site.register(Majeures)
admin.site.register(Campus)
admin.site.register(CustomUser,UserAdmin)
