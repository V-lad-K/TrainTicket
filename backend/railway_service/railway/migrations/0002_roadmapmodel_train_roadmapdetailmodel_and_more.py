# Generated by Django 5.0.6 on 2024-07-11 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmapmodel',
            name='train',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roadmap_train', to='railway.trainmodel'),
        ),
        migrations.CreateModel(
            name='RoadmapDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('departure_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_station_detail', to='railway.stationmodel')),
                ('destination_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_station_detail', to='railway.stationmodel')),
                ('roadmap', models.ManyToManyField(to='railway.roadmapmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='RoadmapTrainModel',
        ),
    ]