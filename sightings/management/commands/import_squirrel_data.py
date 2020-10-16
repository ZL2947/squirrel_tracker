import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Sight
from distutils.util import strtobool

class Command(BaseCommand):
    help = "Import squirrel data from csv file"

    def add_arguments(self,parser):
        parser.add_argument('path',type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as fp:
            reader = csv.DictReader(fp)
            for r in reader:
                sight = Sight(
                    Longitude=r['X'],
                    Latitude=r['Y'],
                    Unique_Squirrel_Id = r['Unique Squirrel ID'],
                    Shift=r['Shift'],
                    Date=r['Date'],
                    Age=r['Age'],
                    Primary_Fur_Color=r['Primary Fur Color'],
                    Location=r['Location'],
                    Specific_Location=r['Specific Location'],
                    Running=strtobool(r['Running']),
                    Chasing=strtobool(r['Chasing']),
                    Climbing=strtobool(r['Climbing']),
                    Eating=strtobool(r['Eating']),
                    Foraging=strtobool(r['Foraging']),
                    Other_Activities=r['Other Activities'],
                    Kuks=strtobool(r['Kuks']),
                    Quaas=strtobool(r['Quaas']),
                    Moans=strtobool(r['Moans']),
                    Tail_Flags=strtobool(r['Tail flags']),
                    Tail_Twitches=strtobool(r['Tail twitches']),
                    Approaches=strtobool(r['Approaches']),
                    Indifferent=strtobool(r['Indifferent']),
                    Runs_From=strtobool(r['Runs from']),
                 )

                sight.save()
