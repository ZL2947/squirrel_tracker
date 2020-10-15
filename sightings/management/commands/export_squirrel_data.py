import csv
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sight

import csv
  
class Command(BaseCommand):
    help = "exports all squirrel data to csv file"

    def add_arguments(self, parser):
            parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'w') as fp:
            attributes = ['Latitude', 
            		  'Longitude', 
            		  'Unique_Squirrel_Id', 
            		  'Shift', 
            		  'Date', 
            		  'Age', 
            		  'Primary_Fur_Color', 
            		  'Location',
                          'Specific_Location',
                          'Running',
                          'Chasing',
                          'Climbing',
                          'Eating',
                          'Foraging',
                          'Other_Activities',
                          'Kuks',
                          'Quaas',
                          'Moans',
                          'Tail_Flags',
                          'Tail_Twitches',
                          'Approaches',
                          'Indifferent',
                          'Runs_From']
            writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Sight.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
