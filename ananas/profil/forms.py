from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
from login.models import Master, Campus, Student, Administration
from string import Template
from django.contrib.auth import get_user_model
import re
from django.utils.safestring import mark_safe
from io import BytesIO
from django.core.files import File
from PIL import Image

User = get_user_model()



class UpdateUserProfil(forms.ModelForm):

    photo = forms.ImageField(required = False)

    class Meta:
        model = User
        fields = ['last_name','first_name','photo','campus']
        widgets = {
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last name','id':'nom'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First name','id':'prenom'}),
            'campus':forms.Select(attrs = {'class': 'form-control', 'id':'campus'}),

        }

    def clean_photo(self):

        """
        Makes thumbnails of given size from given image
        """

        photo = self.cleaned_data['photo']

        if(photo):
            im = Image.open(photo)
            size = 150, 150
            im.thumbnail(size)  # resize image
            rgb_im = im.convert('RGB')

            thumb_io = BytesIO()  # create a BytesIO object

            rgb_im.save(thumb_io, 'JPEG', quality = 100)  # save image to BytesIO object

            new_photo = File(thumb_io, name = photo.name)  # create a django friendly File object

            return new_photo
        else:
            return photo



class UpdateStudentProfil(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['master']
        widgets = {
            'master':forms.Select(attrs = {"class":'form-control','id':'majeure'})
        }

class UpdateAdminProfil(forms.ModelForm):

    class Meta:
        model = Administration
        fields = ['poste','phone']
        widgets = {
            'poste':forms.TextInput(attrs={'class':'form-control','id':'poste'}),
        }
