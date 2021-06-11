from django.db import models


# Create your models here.
class Destination(models.Model):
    city=models.CharField(max_length=50,null=False,blank=False)
    address=models.CharField(max_length=50,null=False,blank=False)
    images=models.ImageField(upload_to='images/destinations',null=False,blank=False)
    