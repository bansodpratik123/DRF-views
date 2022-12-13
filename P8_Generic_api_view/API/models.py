from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField()
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)

class EmpDetails(models.Model):
    phone=models.BigIntegerField()
    state=models.CharField(max_length=32)
    employee=models.ForeignKey(to=Employee, related_name='addresses',null=True, on_delete=models.CASCADE)