from django.contrib.auth.models import AbstractUser, User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    sets = models.ManyToManyField("Set")


class Set(models.Model):
    name = models.TextField(default='')
    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.TextField(default='')
    set = models.ForeignKey(Set, on_delete=models.CASCADE)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    text = models.TextField(default='')
    answer = models.TextField(default='')

