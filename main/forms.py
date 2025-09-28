from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#форма для регистрации
class RegistForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=10, 
        required=True,
        label="Имя"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']

#форма для входа
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")