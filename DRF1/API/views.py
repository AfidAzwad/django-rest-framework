from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
# Model Object - Single Student Data

def Student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)  # it is Dict
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')

# Query Set - All Student Data


def Student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    
    # here serializer is not Dict that's why safe = False
    return JsonResponse(serializer.data, safe=False)
