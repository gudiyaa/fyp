# Generated by Django 2.0.1 on 2018-02-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0015_auto_20180225_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research_publications',
            name='first_corresponding_author',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='research_publications',
            name='three_author',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='research_publications',
            name='two_author',
            field=models.BooleanField(),
        ),
    ]
