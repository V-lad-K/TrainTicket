# Generated by Django 5.0.6 on 2024-07-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoadmapStationModel',
            new_name='RoadmapModel',
        ),
        migrations.RenameField(
            model_name='roadmaptrainmodel',
            old_name='station',
            new_name='roadmap',
        ),
        migrations.AlterField(
            model_name='carriagemodel',
            name='type',
            field=models.CharField(choices=[('S', 'Second class'), ('F', 'First class'), ('L', 'Lux class')], default='S', max_length=1),
        ),
    ]
