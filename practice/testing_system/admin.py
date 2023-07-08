from django.contrib import admin

from .models import Question, Test, Set, Student

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Set)
admin.site.register(Test)
