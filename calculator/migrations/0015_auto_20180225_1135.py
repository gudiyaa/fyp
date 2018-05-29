# Generated by Django 2.0.1 on 2018-02-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0014_research_publications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research_publications',
            name='impact_factor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='research_publications',
            name='no_of_authors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='research_publications',
            name='single_author',
            field=models.BooleanField(),
        ),
    ]
