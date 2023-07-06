from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Question(models.Model):
    text = models.TextField
    answer = models.TextField(default='')


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()