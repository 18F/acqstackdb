from django.shortcuts import render
from django.http import HttpResponse
from .models import Acquisition

# Create your views here.
def home(request):
    acquisitions = Acquisition.objects.all()
    return render(request, "acquisitions/index.html", {"acquisitions":acquisitions})
