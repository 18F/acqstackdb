from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Acquisition, Step, Stage, Track, Actor
from acquisitions import forms
from collections import OrderedDict


# Create your views here.
def home(request):
    acquisitions = Acquisition.objects.all()
    tracks = Track.objects.all()
    stages = Stage.objects.all()
    steps = Step.objects.all()
    data = OrderedDict()
    data["Overall"] = {}
    actors = Actor.objects.all()

    for track in tracks:
        data[track.name] = {}
        for stage in stages:
            data[track.name][stage.order] = {
                "name": stage.name,
                "wip_limit": stage.wip_limit,
                "total": acquisitions.filter(step__stage=stage),
                "steps": {}
            }
            data["Overall"][stage.order] = {
                "name": stage.name,
                "wip_limit": stage.wip_limit,
                "total": acquisitions.filter(step__stage=stage),
                "steps": {}
            }

    for step in steps:
        for s in step.steptrackthroughmodel_set.all():
            data[s.track.name][s.step.stage.order]["steps"][s.order] = {
                "name": s.step.actor.name,
                "wip_limit": s.wip_limit,
                "acquisitions": []
            }
            data["Overall"][s.step.stage.order]["steps"][s.order] = {
                "name": s.step.actor.name,
                "wip_limit": s.wip_limit,
                "acquisitions": []
            }

    for a in acquisitions:
        acq_step = a.step.steptrackthroughmodel_set.get(
            track=a.track
        )
        data[acq_step.track.name][acq_step.step.stage.order]["steps"][acq_step.order]["acquisitions"].append(a)

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
    form = forms.HiddenStageForm(request.POST or None)
    all_stages = Stage.objects.all()
    if form.is_valid():
        stage = Stage.objects.get(name=request.POST.__getitem__('name'))
        if request.POST.__contains__('up'):
            stage.up()
        elif request.POST.__contains__('down'):
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
