from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("student/home", views.student_home_view, name="studentHome"),
    path("student/programs/<int:program_id>", views.program_description_view, name="programDescription"),
    path("student/programs/<int:program_id>/all", views.program_tests_view, name="programTests"),
    path("student/programs/test/<int:test_id>/<int:question_count>", views.test_view, name="test"),
    path("student/programs/desc/<int:test_id>", views.test_description_view, name="testDescription"),
    path("student/progress", views.progress_view, name="progress"),
    path("student/result/<int:test_id>", views.result_view, name="result"),
    path("author/home", views.author_home_view, name="authorHome"),
    path("author/test/new", views.test_new_view, name="testNew"),
    path("author/test/<int:test_id>", views.test_created_view, name="testCreated"),
    path("author/test/form", views.test_form_view, name="testForm"),
    path("author/programs", views.author_programs_view, name="authorPrograms"),
    path("author/programs/new", views.program_new_view, name="programNew"),
    path("teacher/home", views.teacher_home_view, name="teacherHome"),
    path("teacher/programs", views.teacher_programs_view, name="teacherPrograms"),
    path("teacher/students", views.teacher_students_view, name="teacherStudents"),
    path("teacher/students/new", views.students_new_view, name="studentNew"),
]