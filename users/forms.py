from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
import logging
from users.models import User

logger = logging.getLogger(__name__)


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if self.errors.get(field_name):
                field.widget.attrs["class"] += "is-invalid"

        custom_attrs = {
            "username": {
                "label": "Email",
                "placeholder": "Введите email",
                "type": "email",
            },
            "password": {
                "label": "Пароль",
                "placeholder": "Введите пароль",
                "type": "password",
            },
        }
        for field_name, attrs in custom_attrs.items():
            if field_name in self.fields:
                for attr, value in attrs.items():
                    if attr == "label":
                        self.fields[field_name].label = value
                    else:
                        self.fields[field_name].widget.attrs[attr] = value

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)
        if user is None:
            raise forms.ValidationError('Неверный email или пароль')
        self.confirm_login_allowed(user)
        return self.cleaned_data

