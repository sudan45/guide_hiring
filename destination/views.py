from django.shortcuts import render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializer import DestinationsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

class Destinations(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,id):
        return Response(status=403, data={"msg": "API not allowed."})

    @csrf_exempt
    def post(self,request):
        serializer=DestinationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"msg":"Destination is created"},status=201)
        else:
            return Response(data={"msg":"Unable to create the Destinations"},status=403)

