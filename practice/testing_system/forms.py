from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field','placeholder':'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field','placeholder':'Пароль'}))
class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]