from .models import Student,Course
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    student_info = StudentSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = '__all__'

