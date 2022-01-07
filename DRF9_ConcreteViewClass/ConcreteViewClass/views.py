from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Concrete View Class
class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
