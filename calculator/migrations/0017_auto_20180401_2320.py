# Generated by Django 2.0.1 on 2018-04-01 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0016_auto_20180225_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research_publications',
            name='first_corresponding_author',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='impact_factor',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_authors',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_books_published',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_conference_papers',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_journals',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_papers_sci_journal',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_papers_scopus_journal',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_professional_training_received',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_seminars',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_short_courses',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='no_of_sponsored_research_project',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='score',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='single_author',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='three_author',
        ),
        migrations.RemoveField(
            model_name='research_publications',
            name='two_author',
        ),
    ]