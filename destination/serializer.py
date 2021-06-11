from django.db import models
from rest_framework import serializers
from .models import Destination




class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Destination
        fields=('city','address','images')
