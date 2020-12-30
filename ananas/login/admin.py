from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Campus,Majeure,Etudiant,Administration
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

User = get_user_model()

# a modelAdmin class is a representation of a model in the admin interface

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    we provide a custom admin for the User model
    work for all views : delete, add, change, change list, history
    """
    
    # ModelForm presented on both the add/change pages
    # we can also customize the default with the get_form() method
    #form = CustomUserChangeForm

    # these fields shouldn't be changed when a User is created or updated
    readonly_fields = [
        'date_joined',
        'last_login'
    ]

    empty_value_display = 'None'

    # fields displayed in the admin site of the model (change list view)
    list_display = (
        'email',
        'first_name',
        'last_name', 
        'is_staff', 
        'is_active',
        'is_superuser',
        'is_etudiant',
        'is_autre'
        )

    # to activate filter in the right sidebar (change list view)
    list_filter = (
        'is_staff',
        'is_active',
        'is_etudiant',
        'is_autre')

    # control the layout of admin change page
    # (name:str, field_option = dict)
    # the dict key : fields, classes, description
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','user_permissions')}),
        (('Groups'), {'fields': ('groups',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # list of fields name on the model which can be edited on the change list page
    # list_editable =  (
    #      'first_name',
    #      'last_name', 
    # )

    # control which attribute from list_display should be a link to the change page for the model
    list_display_links = (
        'email',
    )

    # fieldset for the add page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name','password1', 'password2', 'is_staff', 'is_active','is_superuser','is_etudiant','is_autre')}
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','user_permissions')}),
        (('Groups'), {'fields': ('groups',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

    # enable a search box on the admin change list page
    search_fields = ['email']

    ordering = ('email',)


    def get_readonly_fields(self,request,obj=None):
        # if obj = None that means we are in the add page
        if obj in request.GET:
            return self.readonly_fields
        else:
            return ['date_joined','last_login','password']
            

    # when we create a user, if we hit the save button the model is saved
    # and we are redirected to the change list view
    def response_add(self,request,obj,post_url_continue=None):

        if '_continue' not in request.POST and '_addanother' not in request.POST:

            return HttpResponseRedirect(reverse("admin:login_customuser_changelist"))

        else:

            return super(CustomUserAdmin,self).response_add(request,obj,post_url_continue)


admin.site.register(Campus)
admin.site.register(Majeure)
admin.site.register(Etudiant)
admin.site.register(Administration)
