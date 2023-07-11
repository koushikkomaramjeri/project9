from django.db import models
class Reg(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    emailid=models.EmailField()
    mobileno=models.IntegerField()
