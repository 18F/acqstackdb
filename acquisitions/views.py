from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Acquisition, Step, Stage, Track, Actor
from acquisitions import forms


# Create your views here.
def home(request):
    acquisitions = Acquisition.objects.all()
    tracks = Track.objects.all()
    stages = Stage.objects.all()
    steps = Step.objects.all()
    data = {}
    actors = Actor.objects.all()

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

    for acquisition in acquisitions:
        data[acquisition.track.name][acquisition.step.stage.order]["steps"][acquisition.step.order]["acquisitions"].append(acquisition)

    return render(request, "acquisitions/index.html", {
        "data": data,
        "actors": actors
    })


@login_required
def acquisition(request, id):
    acquisition = get_object_or_404(Acquisition.objects.filter(id=id))
    return render(request, 'acquisitions/acquisition.html', {
        'acquisition': acquisition,
        'statuses': Step.objects.all()
        })


@login_required
def edit_acquisition(request, id):
    instance = Acquisition.objects.get(id=id)
    form = forms.AcquisitionForm(request.POST or None, instance=instance)
    if form.is_valid():
        report = form.save()
        return redirect(acquisition, id=id)
    return render(request, "acquisitions/new.html", {
        'form': form,
        'item': 'Edit acquisition',
        'action': '/acquisition/'+id+'/edit'
    })


@login_required
def stages(request):
    print(request.POST)
    form = forms.HiddenStageForm(request.POST or None)
    all_stages = Stage.objects.all()
    if form.is_valid():
        stage = Stage.objects.get(name=request.POST.__getitem__('name'))
        if request.POST.__contains__('up'):
            print('moving stage up')
            stage.up()
        elif request.POST.__contains__('down'):
            print('moving stage down')
            stage.down()
        return redirect(stages)
    return render(request, 'acquisitions/stages.html', {
        'form': form,
        'stages': all_stages
    })


@login_required
def new_index(request):
    return render(request, 'acquisitions/new_index.html')


@login_required
def new(request, item):
    forms_dict = {
        "acquisition": forms.AcquisitionForm(request.POST or None),
        "agency": forms.AgencyForm(request.POST or None),
        "subagency": forms.SubagencyForm(request.POST or None),
        "stage": forms.StageForm(request.POST or None),
        "step": forms.StepForm(request.POST or None),
        "track": forms.TrackForm(request.POST or None),
        "actor": forms.ActorForm(request.POST or None)
    }
    try:
        form = forms_dict[item]
    except:
        return render(request, "404.html")
    if form.is_valid():
        report = form.save()
        return redirect(home)
    return render(request, "acquisitions/new.html", {
        'form': form,
        'item': 'New '+item,
        'action': '/new/'+item
        })


def logout_view(request):
    logout(request)
    return redirect('home')
