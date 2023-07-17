from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, TestForm, ProgramForm, QuestionForm
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
@permission_required('testing_system.view_result')
def student_home_view(request):
    student = Student.objects.get(user=request.user)
    programs = student.programs.all()
    return render(request, 'testing_system/studentHome.html', context={'programs': programs})


@login_required
@permission_required('testing_system.add_test')
def author_home_view(request):
    return render(request, 'testing_system/authorHome.html')


@login_required
@permission_required('testing_system.add_student')
def teacher_home_view(request):
    return render(request, 'testing_system/teacherHome.html')


@login_required
@permission_required('testing_system.view_result')
def program_description_view(request, program_id):
    program = Program.objects.get(id=program_id)
    tests = program.test_set.order_by('deadline')[0:2].all()
    title = program.name
    return render(request, 'testing_system/programDescription.html',
                  context={'program': program, 'tests': tests, 'title': title})


@login_required
@permission_required('testing_system.view_result')
def test_view(request, test_id, question_count):
    test = Test.objects.get(id=test_id)
    student = Student.objects.get(user=request.user)
    result = student.result_set.filter(test=test).first()
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


@login_required
@permission_required('testing_system.view_result')
def program_tests_view(request, program_id):
    program = Program.objects.get(id=program_id)
    tests = Test.objects.filter(program=program).all()
    return render(request, 'testing_system/programTests.html',
                  context={'program': program, 'tests': tests})


@login_required
@permission_required('testing_system.view_result')
def test_description_view(request, test_id):
    test = Test.objects.get(id=test_id)
    student = Student.objects.get(user=request.user)
    status = test.result_set.filter(student=student).exists()
    countQuestions = test.question_set.count()
    if request.method == 'POST':
        result = Result.objects.create(test=test, student=student)
        result.save()
        return redirect('/student/programs/test/' + str(test_id) + '/1')
    else:
        if status == True:
            result = test.result_set.filter(student=student).first()
            countResult = result.choice_set.filter(is_correct=True).count()
        else:
            countResult = 0
    return render(request, 'testing_system/testDescription.html',
                  context={'test': test,
                           'status': status,
                           'countQuestions': countQuestions,
                           'countResult': countResult
                           })


@login_required
@permission_required('testing_system.add_test')
def test_new_view(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save()
            return redirect('/author/test/' + str(test.id))
    else:
        form = TestForm()
    return render(request, 'testing_system/testNew.html', context={'form': form})


@login_required
@permission_required('testing_system.add_test')
def test_created_view(request, test_id):
    test = Test.objects.get(id=test_id)
    return render(request, 'testing_system/testCreated.html', context={'test': test})


@login_required
@permission_required('testing_system.add_test')
def test_form_view(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            count = test.question_set.count() + 1
            text = form.cleaned_data['text']
            question = Question.objects.create(text=text, test=test, countQuestion=count)
            answer1 = form.cleaned_data['answer1']
            is_correct1 = form.cleaned_data['is_correct1']
            answer_model1 = Answer.objects.create(is_correct=is_correct1, question=question, text=answer1)
            answer2 = form.cleaned_data['answer2']
            is_correct2 = form.cleaned_data['is_correct2']
            answer_model2 = Answer.objects.create(is_correct=is_correct2, question=question, text=answer2)
            answer3 = form.cleaned_data['answer3']
            is_correct3 = form.cleaned_data['is_correct3']
            answer_model3 = Answer.objects.create(is_correct=is_correct3, question=question, text=answer3)
            answer4 = form.cleaned_data['answer4']
            is_correct4 = form.cleaned_data['is_correct4']
            answer_model4 = Answer.objects.create(is_correct=is_correct4, question=question, text=answer4)
            answer5 = form.cleaned_data['answer5']
            is_correct5 = form.cleaned_data['is_correct5']
            answer_model5 = Answer.objects.create(is_correct=is_correct5, question=question, text=answer5)
            question.save()
            return redirect('/author/test/' + str(test_id))
    else:
        form = QuestionForm()
    return render(request, 'testing_system/testForm.html', context={'test': test, 'form': form})


@login_required
@permission_required('testing_system.view_result')
def progress_view(request):
    student = Student.objects.get(user=request.user)
    programs = student.programs.all()
    return render(request, 'testing_system/progress.html', context={'programs': programs})


@login_required
@permission_required('testing_system.view_result')
def result_view(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(id=test_id)
        student = Student.objects.get(user=request.user)
        result = test.result_set.get(student=student)
        result.total = result.choice_set.filter(is_correct=True).count()
        result.save()
    return HttpResponseRedirect('/student/programs/desc/' + str(test_id))


@login_required
@permission_required('testing_system.add_test')
def author_programs_view(request):
    programs = request.user.program_set.all()
    return render(request, 'testing_system/authorPrograms.html', context={'programs': programs})


@login_required
@permission_required('testing_system.add_test')
def program_new_view(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        program = form.save()
        program.author = request.user
        program.save()
        return redirect('/author/programs')
    else:
        form = ProgramForm()
    return render(request, 'testing_system/programNew.html', context={'form': form})


@login_required
@permission_required('testing_system.add_student')
def teacher_programs_view(request):
    programs = Program.objects.all()
    return render(request, 'testing_system/teacherPrograms.html', context={'programs': programs})


@login_required
@permission_required('testing_system.add_student')
def teacher_students_view(request):
    students = request.user.student_set.all()
    return render(request, 'testing_system/teacherStudents.html', context={'students': students})


@login_required
@permission_required('testing_system.add_student')
def students_new_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(user=user, teacher=request.user)
            group = Group.objects.get(name='student')
            user.groups.add(group)
            user.save()
            student.save()
            return redirect('/teacher/students')
    else:
        form = RegistrationForm()
    return render(request, 'testing_system/studentNew.html', context={'form': form})


@login_required
@permission_required('testing_system.add_student')
def students_delete_view(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        student.user.delete()
        student.delete()
    return HttpResponseRedirect('/teacher/students')


@login_required
@permission_required('testing_system.add_student')
def list_students_view(request, program_id):
    program = Program.objects.get(id=program_id)
    return render(request, 'testing_system/listStudent.html', context={'program': program})


@login_required
@permission_required('testing_system.add_student')
def add_student_program_view(request, program_id):
    program = Program.objects.get(id=program_id)
    return render(request, 'testing_system/addStudentProgram.html', context={'program': program})


@login_required
@permission_required('testing_system.add_student')
def adding_student_view(request, program_id, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        program = Program.objects.get(id=program_id)
        student.programs.add(program)
        student.save()
    return HttpResponseRedirect('/teacher/programs/' + str(program_id))


@login_required
@permission_required('testing_system.add_student')
def delete_student_program_view(request, program_id, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        program = Program.objects.get(id=program_id)
        student.programs.remove(program)
        student.save()
    return HttpResponseRedirect('/teacher/programs/' + str(program_id))
