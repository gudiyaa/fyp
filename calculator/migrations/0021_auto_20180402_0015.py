# Generated by Django 2.0.1 on 2018-04-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0020_research_publications_impact_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research_publications',
            name='score',
            field=models.IntegerField(),
        ),
    ]
