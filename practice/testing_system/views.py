from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, TestForm
from .models import Student, Set, Test


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
    set = Set.objects.get(id=set_id)
    tests = Test.objects.filter(set=set).order_by('deadline')[0:2].all()
    return render(request, 'testing_system/setDescription.html', context={'set': set, 'tests': tests})


def test_view(request, test_id):
    test = Test.objects.get(id=test_id)
    return render(request, 'testing_system/test.html', context={'test': test})


def set_tests_view(request, set_id):
    set = Set.objects.get(id=set_id)
    tests = Test.objects.filter(set=set).all()
    return render(request, 'testing_system/setTests.html', context={'set': set, 'tests': tests})


def test_description_view(request, test_id):
    test = Test.objects.get(id=test_id)
    return render(request, 'testing_system/testDescription.html', context={'test': test})


def test_new_view(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save()
            return redirect('/author/test/' + str(test.id))
    else:
        form = TestForm()
    return render(request, 'testing_system/testNew.html', context={'form': form})


def test_created_view(request, test_id):
    return render(request, 'testing_system/testCreated.html')


def test_form_view(request):
    return render(request, 'testing_system/testForm.html')


def progress_view(request):
    return render(request, 'testing_system/progress.html')

def set_programs_view(request):
    return render(request, 'testing_system/setPrograms.html')


def program_new_view(request):
    return render(request, 'testing_system/programNew.html')

def teacher_programs_view(request):
    return render(request, 'testing_system/setTPrograms.html')

def teacher_students_view(request):
    return render(request, 'testing_system/setStudents.html')

def students_new_view(request):
    return render(request, 'testing_system/studentNew.html')

