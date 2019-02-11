from django.shortcuts import render
from .models import Job


# Create your views here.
def get_index(request):
    jobs = Job.objects
    return render(request, 'index.html', {'jobs': jobs})
