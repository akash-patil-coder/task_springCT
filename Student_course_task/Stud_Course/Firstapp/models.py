from django.db import models
from phone_field import PhoneField

# Create your models here.

class Student(models.Model):
    Roll_no = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone = PhoneField(blank=True,help_text='Contact phone number')


    def __str__(self):
        return str(self.Roll_no)

class Course(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student_info')
    Course_Name = models.CharField(max_length=30)
    Professor_Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)

    def __str__(self):
        return self.Course_Name