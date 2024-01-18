from django.urls import path
from .views import login_user, logout_user, register_user
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from .forms import PasswordResetFormUser, SetPasswordFormUser

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('password-reset/',
         PasswordResetView.as_view(template_name='user/password-reset.html', form_class=PasswordResetFormUser),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
                                          form_class=SetPasswordFormUser),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),

]
