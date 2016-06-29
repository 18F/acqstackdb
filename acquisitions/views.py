from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Acquisition, Step, Stage, Track, Actor
from .forms import AcquisitionForm


# Create your views here.
def home(request):
    acquisitions = Acquisition.objects.all()
    tracks = Track.objects.all()
    stages = Stage.objects.all()
    steps = Step.objects.all()
    data = {}
    actors = Actor.objects.all()

    # print(stages)
    for track in tracks:
        data[track.name] = {}
        for stage in stages:
            data[track.name][stage.order] = {
                "name": stage.name,
                "steps": {}
            }

    for step in steps:
        for track in step.track.all():
            data[track.name][step.stage.order]["steps"][step.order] = {
                "name": step.actor.name,
                "acquisitions": []
            }
            # data[track.name][step.stage.order]["actors"][step.order] = step.actor.name

    for acquisition in acquisitions:
        data[acquisition.track.name][acquisition.step.stage.order]["steps"][acquisition.step.order]["acquisitions"].append(acquisition)

    # print(data)
    return render(request, "acquisitions/index.html", {
        "data": data,
        "actors": actors
    })


# @login_required
def acquisition(request, id):
    acquisition = get_object_or_404(Acquisition.objects.filter(id=id))
    return render(request, 'acquisitions/acquisition.html', {
        'acquisition': acquisition,
        'statuses': Step.objects.all()
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
