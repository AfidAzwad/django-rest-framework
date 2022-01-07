from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# @api_view()
# def Hello_world(request):
#     return Response({'msg' : 'This is GET request !'})

@api_view(['GET','POST'])
def Hello_world(request):
    if request.method == 'GET':
     return Response({'msg' : 'This is GET request !'})
    if request.method == 'POST':
        return Response({'msg' : 'This is POST request !', 'data': request.data})

        
    
