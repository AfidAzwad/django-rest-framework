from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework import status

# Class Based API View
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created !'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_ERROR)

    def put(self, request, pk=None, format=None):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated !'} )
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated !'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted !'})
