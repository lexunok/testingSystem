from django.db import models


class Question(models.Model):
    text = models.TextField
    answer = models.TextField(default='')
