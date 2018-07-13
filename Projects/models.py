from django.db import models
class Projects(models.Model):
    image=models.ImageField(upload_to="images/")
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=10000)
    duration=models.CharField(max_length=300)
