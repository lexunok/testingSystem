from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='+')
    teacher = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    programs = models.ManyToManyField("Program")


class Program(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Test(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    deadline = models.DateField(null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    total = models.BigIntegerField(default=0)


class Question(models.Model):
    countQuestion = models.BigIntegerField(default=0)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    text = models.TextField(default='')


class Choice(models.Model):
    result = models.ForeignKey(Result, null=True, on_delete=models.CASCADE)
    countQuestion = models.BigIntegerField(default=0)
    is_correct = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(default='')
    is_correct = models.BooleanField(default=False)
