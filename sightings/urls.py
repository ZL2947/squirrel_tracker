from django.urls import path

from . import views

urlpatterns = [
        path('',views.homepage),
        path('map/',views.map),
        path('sightings/',views.sighting),
        path('sightings/add/',views.add_squirrel),
        path('sightings/<str:Unique_Squirrel_Id>/',views.update),
         path('sightings/stats/',views.stats),
        ]
