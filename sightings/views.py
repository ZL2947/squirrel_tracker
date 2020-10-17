from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect,get_object_or_404
from .forms import SightForm
# Create your views here.

def homepage(request):
    return render(request,'sightings/homepage.html')

def map(request):
    sights = Sight.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'sightings/map.html',context)

def sighting(request):
    squirrel = Sight.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift','Age']
    context = {
            'squirrels': squirrel,
            'fields':fields
        }
    return render(request, 'sightings/list.html',context)

def add_squirrel(request):
    if request.method == "POST":
        form= SightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()
    context ={
            'form':form,
        }
    return render(request,'sightings/add.html',context)

def update(request,Unique_Squirrel_Id):
    squirrel = Sight.objects.filter(Unique_Squirrel_Id=Unique_Squirrel_Id).first()
    if request.method == 'POST':
        form = SightForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightForm(instance = squirrel)

    context = {
            'form':form,
            }
    return render(request, 'sightings/update.html', context)

def stats(request):
    squirrels = Sight.objects.all()
    squirrel_count = len(squirrels)
    adult = Sight.objects.filter(Age='Adult').aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    am_shift = Sight.objects.filter(Shift='AM').aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    pm_shift = Sight.objects.filter(Shift='PM').aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    running = Sight.objects.filter(Running=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    climbing = Sight.objects.filter(Climbing=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    eating = Sight.objects.filter(Eating=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    foraging = Sight.objects.filter(Foraging=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    kuks = Sight.objects.filter(Kuks=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    quaas = Sight.objects.filter(Quaas=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    moans = Sight.objects.filter(Moans=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    tail_flags = Sight.objects.filter(Tail_Flags=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    tail_twitches = Sight.objects.filter(Tail_Twitches=True).aggregate(Count('Unique_Squirrel_ID'))['Unique_Squirrel_ID_count']
    context = {
        'Total': squirrel_count,
        'Adult Squirrels': adult,
        'AM Shifts': am_shift,
        'PM Shifts':pm_shift,
        'Running Squirrels':running,
        'Climbing Squirrels': climbing,
        'Eating Squirrels': eating,
        'Foraging Squirrels': foraging,
        'Squirrels with Kuks': kuks,
        'Squirrels with Quaas': quaas,
        'Squirrels with Moans': moans,
        'Squirrels with flagging tail': tail_flags,
        'Squirrels with twitching tail': tail_twitch
        }
    return render(request, 'sightings/stats.html', context)
