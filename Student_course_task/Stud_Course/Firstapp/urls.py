from django.urls import path
from .views import addStudent,addCourse,CourseDetails,ShowStudent,DeleteStudent


urlpatterns = [
    path('addStud/',addStudent.as_view()),
    path('addCourse/',addCourse.as_view()),
    path('Coursedetails/',CourseDetails.as_view()),
    path('studCourse/',ShowStudent.as_view()),
    path('deleteStud/<int:Roll_no>/',DeleteStudent.as_view())
]