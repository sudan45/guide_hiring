from django.shortcuts import render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializer import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import login, logout, authenticate
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, authentication_classes,permission_classes




# Create your views here.
class Userviewset(viewsets.ViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        return Response(status=403, data={"msg": "API not allowed."})

    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
            return Response(data={"msg":"Data has been created"})
        else:
            return Response(data={"msg":"Unable to create the data"},status=403)

   
    def update(self, request, id=None):
        user=self.model.objects.get(id=id)
        serializer=self.serializer_class(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"msg":"Data has been created"})
        else:
            return Response(data={"msg":"Unable to update the data"},status=403)

    
@api_view(['POST'])
def login(request):

    data = request.data
    user = authenticate(request, username=data['username'], password=data['password'])

    if user is None:
        return JsonResponse({'error':'No user found'})
    else:
        print(user.role)
        return JsonResponse({'msg': 'Logged in' },status=201)



