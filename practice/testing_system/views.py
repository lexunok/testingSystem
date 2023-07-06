from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


def index(request):
    return render(request, 'testing_system/index.html')


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
    else:
        form = LoginForm()
    return render(request, 'testing_system/login.html', {'form': form})


def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'testing_system/register.html', {'form': form})

def homeView(request):
    programs = ["Математический анализ","Алгебра и геометрия","Дискретная математика","Без темы"]
    return render(request, 'testing_system/home.html', context={'programs': programs})


def setView(request, set_id):
    return render(request, 'testing_system/set.html')


def testView(request, set_id, test_id):
    return render(request, 'testing_system/test.html')
