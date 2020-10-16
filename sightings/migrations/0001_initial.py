# Generated by Django 3.1.2 on 2020-10-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Longitude', models.FloatField(help_text='Longitude of the sight')),
                ('Latitude', models.FloatField(help_text='Latitude of the sight')),
                ('Unique_Squirrel_Id', models.CharField(help_text='The unique ID of the squirrel', max_length=100, unique=True)),
                ('Shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Whether the sight is in the morning or late afternoon?', max_length=16)),
                ('Date', models.IntegerField(blank=True, help_text='Please type sighting date', null=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age of the squirrel', max_length=16)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), (None, '')], help_text='Fur color', max_length=16)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), (None, '')], help_text='Location', max_length=128)),
                ('Specific_Location', models.CharField(blank=True, help_text='Additional notes to the location', max_length=128)),
                ('Running', models.BooleanField(default=False, help_text='Running', max_length=10)),
                ('Chasing', models.BooleanField(default=False, help_text='Chasing', max_length=10)),
                ('Climbing', models.BooleanField(default=False, help_text='Climbing', max_length=10)),
                ('Eating', models.BooleanField(default=False, help_text='Eating', max_length=10)),
                ('Foraging', models.BooleanField(default=False, help_text='Foraging', max_length=10)),
                ('Other_Activities', models.CharField(blank=True, help_text='Other Activities', max_length=128, null=True)),
                ('Kuks', models.BooleanField(default=False, help_text='Kuks', max_length=10)),
                ('Quaas', models.BooleanField(default=False, help_text='Quaas', max_length=10)),
                ('Moans', models.BooleanField(default=False, help_text='Moans', max_length=10)),
                ('Tail_Flags', models.BooleanField(default=False, help_text='Tail_Flags', max_length=10)),
                ('Tail_Twitches', models.BooleanField(default=False, help_text='Tail_Twitches', max_length=10)),
                ('Approaches', models.BooleanField(default=False, help_text='Approaches', max_length=10)),
                ('Indifferent', models.BooleanField(default=False, help_text='Indifferent', max_length=10)),
                ('Runs_From', models.BooleanField(default=False, help_text='Runs_From', max_length=10)),
            ],
        ),
    ]
