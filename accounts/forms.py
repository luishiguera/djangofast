from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class CustomSignUpForm(UserCreationForm):

    class Meta:
        model = USER_MODEL
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthForm(AuthenticationForm):

    class Meta:
        model = USER_MODEL
        fields = ('username', 'password')