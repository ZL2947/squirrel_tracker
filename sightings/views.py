from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect
from .forms import SightForm
# Create your views here.

def homepage(request):
    return render(request,'sightings/homepage.html')

def map(request):
    sights = Sight.object.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'sightings/map.html',context)

def sighting(request):
    squirrel = Sight.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift','Age']
    context = {
            'squirrels': squirrel,
            'fields':field
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
    squirrel = Sight.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
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
