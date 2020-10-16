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
            writer = csv.writer(fp)
            fields = Sight._meta.fields
            for row in Sight.objects.all():
                r = [getattr(row,field.name) for field in fields]
                writer.writerow(r)
            fp.close()
