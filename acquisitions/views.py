from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Acquisition
from .forms import AcquisitionForm

# Create your views here.
def home(request):
    acquisitions = Acquisition.objects.all().order_by('award_status')
    return render(request, "acquisitions/index.html", {"acquisitions":acquisitions})

def new(request):
    form = AcquisitionForm(request.POST or None)
    if form.is_valid():
        report = form.save()
        return redirect(home)
    return render(request, "acquisitions/new.html", {'form': form})
