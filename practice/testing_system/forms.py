from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import Student

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field','placeholder':'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field','placeholder':'Пароль'}))
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]