from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
<<<<<<< HEAD
            email = kwargs['email']
=======
            email=kwargs['email']
            print(email)
>>>>>>> c6d4e4d931dfa6349270095376d9401c94bc5fa8
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
