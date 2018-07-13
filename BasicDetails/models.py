from django.db import models
class BasicDetails(models.Model):
    image=models.ImageField(upload_to="images/")
    name=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=15)
    email=models.CharField(max_length=65)
    currentstatus=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
