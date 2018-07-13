from django.db import models
class Experience(models.Model):
    experience=models.CharField(max_length=500)
    duration=models.IntegerField(max_length=2)
