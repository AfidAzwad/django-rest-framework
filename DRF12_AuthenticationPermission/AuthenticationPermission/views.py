from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Model View Set
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

# Anyone can access to this API because of AllowAny permission
# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]
    
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]