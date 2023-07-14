from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'deadline', 'description')
        widgets = {
            "name": forms.TextInput(attrs={"class": 'testname'}),
            "description": forms.Textarea(attrs={"class": 'testaddition'}),
            "deadline": forms.DateInput(attrs={"class": 'testdate','type': 'date'}),
        }




class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'field','placeholder':'Имя пользователя'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'field','placeholder':'Пароль'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя пользователя'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
