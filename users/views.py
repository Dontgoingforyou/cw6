from django.contrib.auth.views import LoginView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from users.forms import UserRegisterForm, User, EmailAuthenticationForm
from users.services import send_registrations_email, send_verification_email


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('mailing_service:mailing_list')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Пользователь с таким email уже существует')
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        token, created = Token.objects.get_or_create(user=user)
        send_verification_email(user, token, self.request.get_host())
        send_registrations_email(user)
        return redirect('users:verification')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mailing_service:mailing_list')
    form_class = EmailAuthenticationForm

    def form_valid(self, form):
        user = form.user_cache
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


def email_verification(request, token):
    token_instance = get_object_or_404(Token, key=token)
    user = token_instance.user
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
