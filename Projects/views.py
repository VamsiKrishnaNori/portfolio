from django.shortcuts import render
from .models import Projects
def home(request):
    projects=Projects.objects
    return render(request,'BasicDetails/home.html',{'projects':projects})
