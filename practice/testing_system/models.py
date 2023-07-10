from django.contrib.auth.models import AbstractUser, User
from django.db import models



class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='+')
    teacher = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    sets = models.ManyToManyField("Set")


class Set(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Test(models.Model):
    name = models.TextField(default='')
    result = models.BigIntegerField(default=0)
    countQuestions = models.BigIntegerField(default=0)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    text = models.TextField(default='')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(default='')

