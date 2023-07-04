from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'testing_system/index.html')


def login(request):
    return render(request, 'testing_system/login.html')


def student_sets(request):
    programs = ["Математический анализ","Алгебра и геометрия","Дискретная математика","Без темы"]
    return render(request, 'testing_system/student_sets.html', context={'programs': programs})


def set(request, set_id):
    return render(request, 'testing_system/set.html')


def test(request, set_id, test_id):
    return render(request, 'testing_system/test.html')
