from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, TestForm
from .models import Student, Program, Test, Question, Answer, Choice, Result


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
    programs = student.programs.all()
    return render(request, 'testing_system/studentHome.html', context={'programs': programs})


def author_home_view(request):
    return render(request, 'testing_system/authorHome.html')


def teacher_home_view(request):
    return render(request, 'testing_system/teacherHome.html')


def program_description_view(request, program_id):
    program = Program.objects.get(id=program_id)
    tests = program.test_set.order_by('deadline')[0:2].all()
    return render(request, 'testing_system/programDescription.html',
                  context={'program': program, 'tests': tests})


def test_view(request, test_id, question_count):
    test = Test.objects.get(id=test_id)
    student = Student.objects.get(user=request.user)
    result = student.result_set.get(test=test)
    question = test.question_set.get(countQuestion=question_count)
    is_choice = result.choice_set.filter(countQuestion=question_count).exists()
    is_checkbox = question.answer_set.filter(is_correct=True).count() > 1
    questions_list = test.question_set.order_by('countQuestion').all()
    if request.method == 'POST':
        correct_answers = question.answer_set.filter(is_correct=True).count()
        answers = request.POST.getlist('answer')
        choice = Choice.objects.create(result=result, countQuestion=question_count)
        count = 0
        for id in answers:
            answer = question.answer_set.get(id=id)
            if answer.is_correct:
                count += 1
        if count == correct_answers:
            choice.is_correct = True
        choice.save()
        return redirect('/student/programs/test/' + str(test_id) + '/' + str(question_count))
    return render(request, 'testing_system/test.html',
                  context={'test': test,
                           'questionsList': questions_list,
                           'question': question,
                           'is_choice': is_choice,
                           'is_checkbox': is_checkbox
                           })


def program_tests_view(request, program_id):
    program = Program.objects.get(id=program_id)
    tests = Test.objects.filter(program=program).all()
    return render(request, 'testing_system/programTests.html',
                  context={'program': program, 'tests': tests})


def test_description_view(request, test_id):
    test = Test.objects.get(id=test_id)
    student = Student.objects.get(user=request.user)
    status = test.result_set.filter(student=student).exists()
    countQuestions = test.question_set.count()
    if request.method == 'POST':
        result = Result.objects.create(test=test,student=student)
        result.save()
        redirect('/student/programs/test/' + str(test_id) + '/1')
    if status == True:
        result = test.result_set.get(student=student)
        countResult = result.choice_set.filter(is_correct=True).count()
    else:
        countResult = 0
    return render(request, 'testing_system/testDescription.html',
                  context={'test': test,
                           'status': status,
                           'countQuestions':countQuestions,
                           'countResult' : countResult
                           })


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
    student = Student.objects.get(user=request.user)
    programs = student.programs.all()
    return render(request, 'testing_system/progress.html', context={'programs':programs})


def result_view(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(id=test_id)
        student = Student.objects.get(user=request.user)
        result = test.result_set.get(student=student)
        result.total = result.choice_set.filter(is_correct==True).count()
        result.save()



def author_programs_view(request):
    return render(request, 'testing_system/authorProgram.html')


def program_new_view(request):
    return render(request, 'testing_system/programNew.html')


def teacher_programs_view(request):
    return render(request, 'testing_system/teacherPrograms.html')


def teacher_students_view(request):
    return render(request, 'testing_system/programStudents.html')


def students_new_view(request):
    return render(request, 'testing_system/studentNew.html')
