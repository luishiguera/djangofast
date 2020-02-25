from django.urls import path
from accounts.views import Home, SignUp, Login, Logout, ChangePassword, ChangePasswordDone, ResetPassword, ResetPasswordDone, ResetPasswordConfirm, ResetPasswordComplete

app_name = 'accounts'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('change-password-done/', ChangePasswordDone.as_view(), name='change-password-done'),
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path('reset-password-done/', ResetPasswordDone.as_view(), name='reset-password-done'),
    path('reset-password-confirm/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='reset-password-confirm'),
    path('reset-password-complete/', ResetPasswordComplete.as_view(), name='reset-password-complete'),
]