from django.db import models


# Create your models here.

class Expenses(models.Model):
    itemno=models.IntegerField()
    itemname=models.CharField(max_length=64)
    amount=models.IntegerField()
    paidby = models.CharField(max_length=64)
    purchasedate=models.DateField()
    remarks=models.CharField(max_length=256)

# class Login(models.Model):
#     username=models.CharField(max_length=64)
#     password=models.CharField(max_length=64)