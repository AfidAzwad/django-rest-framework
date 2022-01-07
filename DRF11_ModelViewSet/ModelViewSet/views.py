from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

# Model View Set
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# By this only List and Retrieve can be executed
# if we share this API with some restrictions then we can use this
# class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer