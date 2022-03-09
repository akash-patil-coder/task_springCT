from django.shortcuts import render
from .models import Student,Course
from .serializer import StudentSerializer,CourseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class addStudent(APIView):
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class addCourse(APIView):
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CourseDetails(APIView):

    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)




class ShowStudent(APIView):

    def get(self,request):
        stud = Student.objects.all()
        serializer = CourseSerializer(stud,many=True)
        return Response(serializer.data)


class DeleteStudent(APIView):
    def delete(self,request,Roll_no):
        if id:
            try:
                emp = Student.objects.get(Roll_no=Roll_no)
            except Student.DoesNotExist:
                return Response({'msg':'record does not exist'})
            emp.delete()
            return Response({'msg':'record deleted successfully'})