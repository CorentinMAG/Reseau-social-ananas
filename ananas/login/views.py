from django.shortcuts import render,redirect,reverse
from .forms import ConnexionForm,EtudiantForm,AutreForm,Custom_password_reset_form,Custom_password_reset_form_confirm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework.authtoken.models import Token
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User=get_user_model()

def connexion(request):
    """vue pour connecter l'utilisateur"""
    if request.user.is_authenticated:
        if not request.session.get('token'):
            token, _ = Token.objects.get_or_create(user=request.user)
            request.session['token']=token.key
        return redirect(reverse('room', kwargs={'room_name': 'accueil'}))
    else:
        error = False

        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user = authenticate(email=email, password=password)
                if user:
                    if user.is_active:
                        token, _ = Token.objects.get_or_create(user=user)
                        request.session['token']=token.key
                        login(request, user)
                        return redirect(view_redirection)
                else:
                    error = True
        else:
            form = ConnexionForm()

        return render(request, 'login/connexion.html', locals())


def deconnexion(request):
    """vue de déconnexion"""
    logout(request)
    return redirect(reverse(connexion))

@login_required
def view_redirection(request):
    return redirect(reverse('room', kwargs={'room_name': '5'}))


class Forbidden(TemplateView):
    """page interdite"""
    template_name="error403.html"


class test_reset_password_mail(UserPassesTestMixin):
    login_url='/account/error/forbidden'
    def test_func(self):
        if not self.request.session.get('entered_mail'):
            return False
        else:
            return True
    raise_exception=False

class MyPasswordResetView(auth_views.PasswordResetView):
    """vue qui gère l'envoie d'email lors d'une demande
    de mot de passe perdu"""
    template_name="login/password_reset.html"
    form_class=Custom_password_reset_form
    html_email_template_name="login/password_reset_mail.html"
    subject_template_name="login/password_reset_subject.txt"
    success_url='/account/password_reset/done'

    def form_valid(self,form):
        self.request.session['entered_mail']=form.cleaned_data['email']
        return super().form_valid(form)


class MyPasswordResetDoneView(test_reset_password_mail,auth_views.PasswordResetDoneView):
    template_name="login/password_reset_done.html"


class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """Vue qui affiche un formulaire permettant de changer de mot de passe"""
    template_name="login/password_reset_confirm.html"
    form_class=Custom_password_reset_form_confirm

class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """Vue qui est appelé une fois qu'on a fait la
    demande de réinitialisation de mot de passe"""
    template_name="login/password_reset_complete.html"

def RegisterView(request):
    """simple vue qui va permettre à l'utilisateur
    de créer un compte administration ou étudiant"""
    return render(request,"login/choosebetweenadminorstudent.html")

def EtudiantView(request):
    """Vue qui se charge d'afficher le formulaire
    d'inscription pour les étudiants"""
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('login/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Le compte a bien été créé ! Il faut maintenant l\'activer')
            return redirect(reverse('connexion'))
    else:
        form = EtudiantForm()
    return render(request, 'login/register.html', {'form': form})

def AutreView(request):
    """Vue qui va afficher le formulaire
    d'inscription pour l'administration"""
    if request.method == 'POST':
        form = AutreForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activer votre compte Ananas'
            message = render_to_string('login/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Le compte a bien été créé ! Il faut maintenant l\'activer')
            return redirect(reverse('connexion'))
    else:
        form = AutreForm()
    return render(request, 'login/autre.html', {'form': form})


def activate(request, uidb64, token):
    """activation du compte,
    donc on gère l'envoie de l'email ici
    avec le token"""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend='login.EmailBackend.EmailBackend')
        messages.success(request, 'Votre compte a été activé ! vous pouvez maintenant vous connecter')
        return redirect(reverse(connexion))
    else:
        return HttpResponse('Activation link is invalid!')

