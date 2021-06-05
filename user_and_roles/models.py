from django.db.models.enums import Choices
from guide_hiring.settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Role(models.IntegerChoices):
    tourist=1
    guide=0

# Create your models here.
class User(AbstractUser):
    token=models.CharField(max_length=50,null=True,blank=True)
    status=models.BooleanField(default=0)
    name = models.CharField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=50,null=False,blank=False)
    phone = models.BigIntegerField()
    dob = models.DateField()
    image = models.ImageField(upload_to='user/image',null=False)
    role = models.IntegerField(choices=Role.choices)

