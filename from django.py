from django.db import models


class Tutor (models.Model):
    name = models.CharField()
    students = models.OneToManyField(defoult='')


class Author (models.Model)
    name = models.CharField()
    programs = models.OneToManyField(default='')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'nazvanie',}}