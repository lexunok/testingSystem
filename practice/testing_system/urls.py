from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("student/home", views.student_home_view, name="studentHome"),
    path("student/sets/<int:set_id>", views.set_description_view, name="setDescription"),
    path("student/sets/<int:set_id>/all", views.set_tests_view, name="setTests"),
    path("student/sets/test/<int:test_id>", views.test_view, name="test"),
    path("student/sets/desc/<int:test_id>", views.test_description_view, name="testDescription"),
    path("student/progress", views.progress_view, name="progress"),
    path("author/home", views.author_home_view, name="authorHome"),
    path("author/test/new", views.test_new_view, name="testNew"),
    path("author/test/<int:test_id>", views.test_created_view, name="testCreated"),
    path("author/test/form", views.test_form_view, name="testForm"),
    path("teacher/home", views.teacher_home_view, name="teacherHome"),
]