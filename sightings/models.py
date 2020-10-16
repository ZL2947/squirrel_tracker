from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator
# Create your models here.

class Sight(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude of the sight'),)

    Latitude = models.FloatField(
            help_text = _('Latitude of the sight'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = _('The unique ID of the squirrel'),
            max_length = 100,
            unique = True,
            blank = False
            )
    AM = 'AM'
    PM = 'PM'
    SESSION=(
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift = models.CharField(
            help_text = _('Whether the sight is in the morning or late afternoon?'),
            max_length=16,
            choices=SESSION,
            blank=True)

    Date = models.IntegerField(
            help_text = _('Please type sighting date'),
            null = True,
            blank=True)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            )

    Age = models.CharField(
            help_text = _('Age of the squirrel'),
            max_length=16,
            choices = AGE_CHOICE,
            blank = True
            )

    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    COLOR_CHOICE=(
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (None, ''),
            )

    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color'),
            max_length=16,
            choices = COLOR_CHOICE,
            blank = True
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION_CHOICE=(
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, ''),
            )

    Location =  models.CharField(
            help_text = _('Location'),
            max_length=128,
            choices = LOCATION_CHOICE,
            blank = True
            )

    Specific_Location = models.CharField(
            help_text = _('Additional notes to the location'),
            max_length=128,
            blank = True,
            )

    Running = models.BooleanField(
            help_text = _('Running'),
            max_length = 10,
            default=False,
    )

    Chasing = models.BooleanField(
            help_text = _('Chasing'),
            max_length = 10,
            default=False,
    )

    Climbing = models.BooleanField(
            help_text = _('Climbing'),
            max_length = 10,
            default=False,
    )

    Eating = models.BooleanField(
            help_text = _('Eating'),
            max_length = 10,
            default=False,
    )

    Foraging = models.BooleanField(
            help_text = _('Foraging'),
            max_length = 10,
            default=False,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
        blank = True
    )

    Kuks = models.BooleanField(
            help_text = _('Kuks'),
            max_length = 10,
            default=False,
    )

    Quaas = models.BooleanField(
            help_text = _('Quaas'),
            max_length = 10,
            default=False,
    )

    Moans = models.BooleanField(
            help_text = _('Moans'),
            max_length = 10,
            default=False,
    )

    Tail_Flags = models.BooleanField(
            help_text = _('Tail_Flags'),
            max_length = 10,
            default=False,
    )

    Tail_Twitches = models.BooleanField(
            help_text = _('Tail_Twitches'),
            max_length = 10,
            default=False,
    )

    Approaches = models.BooleanField(
            help_text = _('Approaches'),
            max_length = 10,
            default=False,
    )

    Indifferent = models.BooleanField(
            help_text = _('Indifferent'),
            max_length = 10,
            default=False,
    )

    Runs_From = models.BooleanField(
            help_text = _('Runs_From'),
            max_length = 10,
            default=False,
    )
    def __str__(self):
        return self.Unique_Squirrel_Id
