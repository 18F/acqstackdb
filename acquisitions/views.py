from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Acquisition
from .forms import AcquisitionForm

# Create your views here.
def home(request):
    acquisitions = Acquisition.objects.all().order_by('award_status')
    statuses = {}
    for s in Acquisition.AWARD_STATUS_CHOICES:
        statuses[s[0]] = {}
        statuses[s[0]]["title"] = s[1]
        statuses[s[0]]["count"] = 0
        statuses[s[0]]["acquisitions"] = []
    for a in acquisitions:
        statuses[a.award_status]["count"] += 1
        statuses[a.award_status]["acquisitions"].append(a)
    return render(request, "acquisitions/index.html", {
        "statuses":statuses
        })

# @login_required
def acquisition(request, id):
    acquisition = get_object_or_404(Acquisition.objects.filter(id=id))
    return render(request, 'acquisitions/acquisition.html', {
        'acquisition': acquisition,
        'statuses':Acquisition.AWARD_STATUS_CHOICES
        })

@login_required
def new(request):
    form = AcquisitionForm(request.POST or None)
    if form.is_valid():
        report = form.save()
        return redirect(home)
    return render(request, "acquisitions/new.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
