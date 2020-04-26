from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Campus,Majeure,Etudiant,Administration


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','first_name','last_name', 'is_staff', 'is_active','is_superuser','is_etudiant','is_autre','genre')
    list_filter = ('email', 'is_staff', 'is_active','is_etudiant','is_autre')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','user_permissions')}),
        (('Groups'), {'fields': ('groups',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Campus)
admin.site.register(Majeure)
admin.site.register(Etudiant)
admin.site.register(Administration)
