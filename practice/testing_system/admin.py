from django.contrib import admin

from .models import Question, Test, Program, Student, Result, Answer

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Program)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Answer)
