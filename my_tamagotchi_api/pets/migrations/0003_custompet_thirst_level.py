# Generated by Django 5.0.6 on 2024-05-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_custompet_bathroom_level_custompet_friendliness_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompet',
            name='thirst_level',
            field=models.IntegerField(default=0),
        ),
    ]
