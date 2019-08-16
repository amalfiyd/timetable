# Generated by Django 2.2.1 on 2019-08-16 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Subject Title')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Subject Description')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Type Name')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Type Description')),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Group Description'),
        ),
        migrations.CreateModel(
            name='UserSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.UserType', verbose_name='User Type'),
        ),
        migrations.AddField(
            model_name='subject',
            name='users',
            field=models.ManyToManyField(through='timetable.UserSubject', to='timetable.User'),
        ),
    ]
