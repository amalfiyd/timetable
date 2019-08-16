# Generated by Django 2.2.1 on 2019-08-16 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20190816_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField(verbose_name='Start Time')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sun', 'Sunday'), ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], max_length=30, verbose_name='Class Time(Day of Week)')),
                ('hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Time')),
            ],
        ),
    ]
