from django.shortcuts import render, redirect, reverse
from .forms import ConnexionForm, EtudiantForm, AutreForm, Custom_password_reset_form, Custom_password_reset_form_confirm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from rest_framework.authtoken.models import Token
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.utils import timezone

User = get_user_model()


def connexion(request):

    """
    connexion view
    """

    if request.user.is_authenticated:

        request.user.last_login = timezone.now()
        request.user.save()

        # if the user is connected (meaning there is still an active session)
        # we create or retrieve his token
        # then we directly redirect to the timeline page, the user doesn't have to
        # re-enter his credentials
        if not request.session.get('token'):
            token, _ = Token.objects.get_or_create(user=request.user)
            request.session['token'] = token.key

        return redirect(reverse('timeline-home'))

    else:
        error = False

        # handle POST request in the login page
        if request.method == "POST":

            form = ConnexionForm(request.POST)

            if form.is_valid():

                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                stay_connected = form.cleaned_data["stay_connected"]

                # we authenticate the user whith the provided information
                user = authenticate(email=email, password=password)

                if user:
                    if user.is_active:

                        token, _ = Token.objects.get_or_create(user=user)
                        request.session['token'] = token.key

                        if not stay_connected:
                            request.session.set_expiry(0)

                        # we register the user into the current session
                        login(request, user)

                        request.user.last_login = timezone.now()
                        request.user.save()

                        return redirect(reverse('timeline-home'))
                else:
                    error = True
        else:
            # if the request method is not POST we only provide the connexion form to the template
            form = ConnexionForm()

        return render(request, 'login/connexion.html', locals())


def deconnexion(request):

    """
    deconnexion view
    """

    # the current session is wiped out
    logout(request)

    return redirect(reverse('login:connexion'))

def error_404(request, *args, **kwargs):

    """
    view when error404
    """

    return render(request, 'error404.html', {})

def error_500(request,*args,**kwargs):

    """
    view when error500
    """

    return render(request, 'error_500.html', {})

def error_403(request,*arg,**kwargs):

    """
    view when error 403
    """

    return render(request,'error403.html',{})


class MyPasswordResetView(auth_views.PasswordResetView):

    """
    this view send an email to recover password
    """

    template_name = "login/password_reset.html"
    form_class = Custom_password_reset_form
    html_email_template_name = "login/password_reset_mail.html"
    subject_template_name = "login/password_reset_subject.txt"
    success_url = "/account/password_reset/done"

    def form_valid(self, form):
        self.request.session['provided_email'] = form.cleaned_data['email']
        return super().form_valid(form)


class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):

    def get(self,request,*args,**kwargs):
        # we check if there is the variable 'entered_mail' in the current session
        # if not, it means that the user isn't resetting his password 
        # and so this url shouldn't be accessed
        if not request.session.get('provided_email'):
            # raise 403 error and so the error_403 view is triggered
            raise PermissionDenied()
        else:
            # otherwise we just render the template
            return self.render_to_response({})


    template_name = "login/password_reset_done.html"


class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):

    """
    form to change the user password
    """


    template_name = "login/password_reset_confirm.html"
    form_class = Custom_password_reset_form_confirm


class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):

    """
    call when the user has set up his new password
    """

    def get(self,request,*args,**kwargs):
        if not request.session.get('provided_email'):
            raise PermissionDenied()
        else:
            # we remove the 'provided_email' key from the session
            try:
                del request.session['provided_email']
            except KeyError:
                pass
            return self.render_to_response({})


    template_name = "login/password_reset_complete.html"


def RegisterView(request):

    """
    view when we hit the 'sign up' button of the login page
    """

    return render(request, "login/register.html")


def _handleRegistration(request,form,template_name):

    """
    handle registration form
    """

    if request.method == 'POST':

        _form = form(request.POST)
        
        if _form.is_valid():

            # we create the user by calling the save method of the form
            user = _form.save(commit=False)
            user.is_active = False
            user.save()

            # we send email to the user to activate his account
            current_site = get_current_site(request)
            mail_subject = 'Activate your Ananas account'
            message = render_to_string('login/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = _form.cleaned_data.get('email')
            email = EmailMessage(
                subject = mail_subject, body = message, to = [to_email]
            )
            email.content_subtype = "html"
            email.send()

            # the message is save on the session, then we call the connexion view which put retrieve all context
            # variables and display them in the template
            messages.success(request, 'Your account has been created ! Now you need to activate it')
            
            return redirect(reverse('login:connexion'))
    else:

        _form = form()

    return render(request, template_name, {'form': _form})


def StudentView(request):

    """
    handle registration for students
    """

    form = EtudiantForm
    return _handleRegistration(request,form,'login/student.html')



def AdminView(request):

    """
    handle the registration form, similar to the EtudantView
    """
    form = AutreForm
    return _handleRegistration(request,form,'login/admin.html')


def activate(request, uidb64, token):

    """
    activation of the user account
    """

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None

    if user is not None and account_activation_token.check_token(user, token):

        user.is_active = True
        user.save()

        messages.success(request, 'Your account has been activated ! You can now log in')

        return redirect(reverse('login:connexion'))

    else:

        return HttpResponse('Activation link is invalid!')
