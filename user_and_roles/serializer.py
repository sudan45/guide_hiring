from rest_framework import serializers
from .models import User
from rest_framework import exceptions
from django.contrib.auth import authenticate




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password','status','token','name','address','phone','dob','image','role')



