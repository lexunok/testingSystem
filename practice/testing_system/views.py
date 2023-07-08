from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Student


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
            student = Student(user=user)
            group = Group.objects.get(name='student')
            user.groups.add(group)
            student.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()
    return render(request, 'testing_system/register.html', {'form': form})

def homeView(request):
    student = request.user.student
    programs = student.sets.all()
    return render(request, 'testing_system/home.html', context={'programs': programs})


def setDescriptionView(request, set_id):
    return render(request, 'testing_system/setDescription.html')


def testView(request, set_id, test_id):
    return render(request, 'testing_system/test.html')

def testsView(request):
    return render(request, 'testing_system/tests.html')

def testDescriptionView(request):
    return render(request, 'testing_system/testDescription.html')

def progressView(request):
    return render(request, 'testing_system/progress.html')

def profileView(request):
    return render(request, 'testing_system/profile.html')
