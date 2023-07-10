from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("student/home/sets/<int:set_id>", views.set_description_view, name="setdescription"),
    path("student/home/sets/<int:set_id>/<int:test_id>", views.test_view, name="test"),
    path("tests", views.tests_view, name="tests"),
    path("testDesc", views.test_description_view, name="testdescription"),
    path("progress", views.progress_view, name="progress"),
    path("student/home", views.student_home_view, name="studentHome"),
    path("author/home", views.author_home_view, name="authorHome"),
    path("teacher/home", views.teacher_home_view, name="teacherHome"),
]