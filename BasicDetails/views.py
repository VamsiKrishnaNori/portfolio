from django.shortcuts import render
from Projects.models import Projects
from .models import BasicDetails
from Education.models import Education
from Experience.models import Experience
from SkillsAndCertifications.models import SkillsAndCertifications
from publications.models import Publications
def home(request):
    projects=Projects.objects
    basicdetails=BasicDetails.objects
    education=Education.objects
    experience=Experience.objects
    skills=SkillsAndCertifications.objects
    publications=Publications.objects
    return render(request,'BasicDetails/home.html',{'publications':publications,'projects':projects,'basicdetails':basicdetails,'education':education,'experience':experience,'skills':skills})
