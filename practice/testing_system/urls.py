from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("student/sets", views.student_sets, name="student_sets"),
    path("student/sets/<int:set_id>", views.set, name="set"),
    path("student/sets/<int:set_id>/<int:test_id>", views.test, name="test"),
]