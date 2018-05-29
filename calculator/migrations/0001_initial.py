# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-15 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('post_apply', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=50)),
                ('application_no', models.BigAutoField(db_column='APPLICATION_NO', primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=30)),
                ('pwd_status', models.CharField(max_length=5)),
                ('internal_candidate', models.BooleanField()),
                ('profile_image', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('aadhar_card', models.BigIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=20)),
                ('marital_status', models.CharField(max_length=10)),
                ('correspondence_address', models.CharField(max_length=200)),
                ('permanent_address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('areas_of_specialization', models.TextField(max_length=300)),
                ('phd_thesis_title', models.CharField(max_length=200)),
                ('date_of_acquiring_phd', models.DateField()),
            ],
        ),
    ]
