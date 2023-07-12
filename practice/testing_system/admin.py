from django.contrib import admin

from .models import Question, Test, Set, Student, Result, Answer

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Set)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Answer)
