from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.registerView, name="register"),
    path("login/", views.loginView, name="login"),
    path("home/", views.homeView, name="home"),
    path("home/sets/<int:set_id>", views.setView, name="set"),
    path("home/sets/<int:set_id>/<int:test_id>", views.testView, name="test"),
]