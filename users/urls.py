from django.views.generic import TemplateView

from users.apps import UsersConfig
from django.urls import path

from users.views import UserCreateView, email_verification, LogoutView, CustomLoginView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_confirm/<str:token>', email_verification, name='email_confirm'),
    path('email_verification/', TemplateView.as_view(template_name='users/email_verification.html'),
         name='verification'),
]
