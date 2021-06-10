from django.db import models
from rest_framework import serializers
from .models import User,Tourist_Profile,Guide_Profile
from rest_framework import exceptions
from django.contrib.auth import authenticate




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password','status','token','name','address','phone','dob','image','role')



class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guide_Profile
        fields=('user','citizenship','citizenship_number')


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tourist_Profile
        fields=('user','passport','passport_number','description','language')
