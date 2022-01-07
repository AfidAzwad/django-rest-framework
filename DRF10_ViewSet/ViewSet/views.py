from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework import status

# View Set
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created !'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_ERROR)

    def update(self, request, pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated !'} )
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def partial_update(self, request, pk):
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated !'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted !'})
