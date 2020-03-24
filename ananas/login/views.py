from django.shortcuts import render,redirect,reverse
from .forms import ConnexionForm,RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password) 
            if user:  
                login(request, user)  
                return redirect(view_redirection)
            else: 
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'login/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

@login_required
def view_redirection(request):
    return HttpResponse("Vous avez été redirigé {0}.".format(request.user.username))



class MyPasswordResetView(auth_views.PasswordResetView):
	template_name="login/password_reset.html"
	email_template_name="login/password_reset_mail.html"
	subject_template_name="login/password_reset_subject.txt"

class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
	template_name="login/password_reset_done.html"

class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name="login/password_reset_confirm.html"

class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name="login/password_reset_complete.html"

class RegisterView(FormView):
    template_name="login/register.html"
    form_class=RegisterForm
    success_url="/account/connexion"

    def form_valid(self,form):
         form.save()
         messages.success(self.request, 'Le compte a bien été créé !')
         return  super().form_valid(form)

