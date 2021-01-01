import hashlib, os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from actstream import action

from .Manager import CustomUserManager

# blank = True - allow empty value in form
# null = True - empty values are stored as null


class Campus(models.Model):

    """"
    All school's campus
    """

    campus_name = models.CharField(max_length = 30, unique = True)
    address = models.CharField(max_length = 100, blank = True, null = True)

    class Meta:
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.campus_name


class Master(models.Model):
    
    """
    All school's masters 
    """

    master_name = models.CharField(max_length = 50, unique = True)

    class Meta:
        verbose_name_plural = "Masters"

    def __str__(self):
        return self.master_name


class User(AbstractBaseUser, PermissionsMixin):

    """
    The custom UserModel
    """

    email = models.EmailField(_('email address'), unique = True, primary_key = True)
    avatar = models.URLField(max_length = 200)
    photo = models.ImageField(upload_to = 'photoProfile/', null = True, blank = True)
    first_name = models.CharField(max_length = 50, verbose_name = 'First name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last name')
    is_student = models.BooleanField(default = True)
    campus = models.ForeignKey(Campus, on_delete = models.CASCADE, blank = True, null = True)

    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)


    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(null = True)

    USERNAME_FIELD = 'email'

    # fields name required when creating a user via the createsuperuser management command
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()


    def get_full_name(self,first='first_name'):

        """
        Returns the full name of the current instance
        """

        if first == 'first_name':
            full_name = "{} {}".format(self.first_name, self.last_name)
        elif first == 'last_name':
            full_name = "{} {}".format(self.last_name, self.first_name) 

        return full_name

    def __str__(self):
        return self.email


class Student(models.Model):
    
    """
    Student model
    """

    user = models.OneToOneField(User, related_name = "user_student", on_delete = models.CASCADE)
    # promo = models.IntegerField(blank=True)
    # phone = PhoneNumberField(blank=True, verbose_name='numéro de téléphone')
    master = models.ForeignKey(Master, on_delete = models.CASCADE,null = True)

    def __str__(self):
        return self.user.get_full_name()


class Administration(models.Model):
   
    """
    admin model
    """

    user = models.OneToOneField(User, related_name = "user_admin", on_delete = models.CASCADE)
    poste = models.CharField(max_length=255, blank = True, null = True)
    phone = PhoneNumberField(blank = True, verbose_name = 'phone number', null = True)

    def __str__(self):
        return self.user.get_full_name()


@receiver(post_save, sender = User)
def Create_user_avatar(sender, instance, created, **kwargs):
    """
    create user avatar when the user is created
    """

    if created:
        md5_email = hashlib.md5()
        md5_email.update(instance.email.encode('utf8'))
        avatar = "https://www.gravatar.com/avatar/{}?d=identicon".format(md5_email.hexdigest())
        instance.avatar = avatar
        instance.save()
        action.send(instance,verb = "account creation")


@receiver(pre_save,sender = User)
def delete_file_on_change(sender, instance, **kwargs):
    """
    delete from the file system the user old photo
    after updating 
    """

    try:
        old_file = User.objects.get(pk = instance.pk).photo

        new_file = instance.photo

        if old_file != new_file:
            old_file.delete(save = False)
    except:
        pass