from django.urls import path
from .views import UserRegistration
from .views_login import UserLogin
from .view_reset_password import PasswordResetRequest
from .view_password_new import PasswordReset

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('register/<int:id>/',UserRegistration.as_view(), name='user-getbyid'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('delete/<int:id>/', UserRegistration.as_view(), name='user-delete'),
    path('password/reset/request/', PasswordResetRequest.as_view(), name='password-reset-request'),
    path('password/reset/',PasswordReset.as_view(), name='password-reset'),
]