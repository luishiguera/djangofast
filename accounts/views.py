# Or django.contrib.auth import views / views.LoginView...
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from accounts.forms import CustomSignUpForm
from accounts.forms import CustomAuthForm
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class SignUp(CreateView):
    form_class = CustomSignUpForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'signup.html'

class Login(LoginView): # Also Sign In, avoid confusion
    form_class = CustomAuthForm
    template_name = 'login.html'

class Logout(LogoutView):
    pass

class ChangePassword(PasswordChangeView):
    """
    Avoid using done view, it can be recalled instead success_url to home/profile view for example
    from django.contrib.messages.views import SuccessMessageMixin
    SuccessMessageMixin - attr: success_message = "Your password has been change"
    
    html
    {% if messages %}
        {% for message in messages %}
            <div">
                {{ message|safe }}
             </div">
        {% endfor %}
    {% endif %}

    https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#adding-messages-in-class-based-views
    """
    success_url = reverse_lazy('accounts:change-password-done')
    template_name = 'change-password.html'

class ChangePasswordDone(PasswordChangeDoneView):
    template_name = 'change-password-done.html'

class ResetPassword(PasswordResetView):
    """
    Avoid using done view, it can be recalled instead success_url to home or any other view for example
    from django.contrib.messages.views import SuccessMessageMixin
    SuccessMessageMixin - attr: success_message = "We’ve emailed you instructions for setting your password"
    
    html
    {% if messages %}
        {% for message in messages %}
            <div">
                {{ message|safe }}
             </div">
        {% endfor %}
    {% endif %}

    https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#adding-messages-in-class-based-views
    """
    email_template_name = 'reset-password-email.html'
    success_url = reverse_lazy('accounts:reset-password-done')
    template_name = 'reset-password.html'

class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'reset-password-done.html'

class ResetPasswordConfirm(PasswordResetConfirmView):
    """
    Avoid using complete view, it can be recalled instead success_url to home or any other view for example
    from django.contrib.messages.views import SuccessMessageMixin
    SuccessMessageMixin - attr: success_message = "Your password has been set"
    
    html
    {% if messages %}
        {% for message in messages %}
            <div">
                {{ message|safe }}
             </div">
        {% endfor %}
    {% endif %}

    https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#adding-messages-in-class-based-views
    """
    success_url = reverse_lazy('accounts:reset-password-complete')
    template_name = 'reset-password-confirm.html'

class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = 'reset-password-complete.html'