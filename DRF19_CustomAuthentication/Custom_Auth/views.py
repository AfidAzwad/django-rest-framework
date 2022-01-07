from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Custom_Auth.customauth import CustomAuthentication

# Model View Set
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
