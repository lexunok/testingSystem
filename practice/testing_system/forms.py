from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Test, Program


class QuestionForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'testquestion'}))
    answer1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'testanswer','placeholder':'Вариант ответа'}))
    is_correct1 = forms.BooleanField(required=False)
    answer2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'testanswer','placeholder':'Вариант ответа'}))
    is_correct2 = forms.BooleanField(required=False)
    answer3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'testanswer','placeholder':'Вариант ответа'}))
    is_correct3 = forms.BooleanField(required=False)
    answer4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'testanswer','placeholder':'Вариант ответа'}))
    is_correct4 = forms.BooleanField(required=False)
    answer5 = forms.CharField(widget=forms.TextInput(attrs={'class': 'testanswer','placeholder':'Вариант ответа'}))
    is_correct5 = forms.BooleanField(required=False)


class TestForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), widget=forms.Select(attrs={'class': 'program'}))
    class Meta:
        model = Test
        fields = ('name', 'deadline', 'description','program')
        widgets = {
            "name": forms.TextInput(attrs={"class": 'testname'}),
            "description": forms.Textarea(attrs={"class": 'testaddition'}),
            "deadline": forms.DateInput(attrs={"class": 'testdate', 'type': 'date'}),

        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'description')
        widgets = {
            "name": forms.TextInput(attrs={"class": 'programname'}),
            "description": forms.Textarea(attrs={"class": 'programaddition'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Пароль'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя пользователя'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
