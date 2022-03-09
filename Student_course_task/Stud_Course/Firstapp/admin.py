from django.contrib import admin
from .models import Student,Course

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Roll_no','Name','Email','Phone']
admin.site.register(Student,StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['student','Course_Name','Professor_Name','Description']
admin.site.register(Course,CourseAdmin)
