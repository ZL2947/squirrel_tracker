from django.urls import path

from . import views

urlpatterns = [
        path('',views.homepage, name='Home'),
        path('map/',views.map, name='Map'),
        path('sightings/',views.sighting, name='AllSquirrels'),
        path('sightings/add/',views.add_squirrel, name='Add'),
        path('sightings/<str:Unique_Squirrel_Id>/',views.update, name='Update'),
        path('sightings/stats/',views.stats, name='Stats'),
        ]
