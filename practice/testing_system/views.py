from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Student


def index(request):
    return render(request, 'testing_system/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            group = user.groups.first()
            if user and group is not None:
                login(request, user)
                if group.name == 'author':
                    return redirect('/author/home')
                if group.name == 'teacher':
                    return redirect('/teacher/home')
                if group.name == 'student':
                    return redirect('/student/home')
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'testing_system/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/login')
    else:
        form = RegistrationForm()
    return render(request, 'testing_system/register.html', {'form': form})


def student_home_view(request):
    student = Student.objects.get(user=request.user)
    programs = student.sets.all()
    return render(request, 'testing_system/studentHome.html', context={'programs': programs})


def author_home_view(request):
    return render(request, 'testing_system/authorHome.html')


def teacher_home_view(request):
    return render(request, 'testing_system/teacherHome.html')


def set_description_view(request, set_id):
    return render(request, 'testing_system/setDescription.html')


def test_view(request, set_id, test_id):
    return render(request, 'testing_system/test.html')


def tests_view(request):
    return render(request, 'testing_system/tests.html')


def test_description_view(request):
    return render(request, 'testing_system/testDescription.html')


def progress_view(request):
    return render(request, 'testing_system/progress.html')
