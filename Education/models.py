from django.db import models
class Education(models.Model):
    course=models.CharField(max_length=50)
    year=models.IntegerField(max_length=4)
    institute=models.CharField(max_length=65)
    percentage=models.DecimalField(max_digits=4,decimal_places=2)
