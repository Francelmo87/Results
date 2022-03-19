from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Result(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    protocol = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=18, null=True)
    result_1 = models.CharField(max_length=100, null=True)
    result_2 = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.user)