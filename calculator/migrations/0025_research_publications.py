# Generated by Django 2.0.1 on 2018-04-04 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calculator', '0024_auto_20180404_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research_Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rd_onlypi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rd_pi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('no_of_rest_pi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rd_co_pi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rd_onlyinventor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rd_inventor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('no_of_rest_inventor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rd_co_inventor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score2', models.DecimalField(decimal_places=3, max_digits=6)),
                ('no_of_5lakhs', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score3', models.DecimalField(decimal_places=3, max_digits=6)),
                ('phd_sole_supervisor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('phd_first_supervisor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('no_of_rest_supervisor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('phd_co_supervisor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score4', models.DecimalField(decimal_places=3, max_digits=6)),
                ('as_sole_journal_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('as_first_journal_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('no_of_rest_journal_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('as_co_journal_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score5', models.DecimalField(decimal_places=3, max_digits=6)),
                ('as_sole_conf_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('as_first_conf_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('no_of_rest_conf_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('as_co_conf_author', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score6', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_hod', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_dean', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_cw', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_tpi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_advisor', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_cvo', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_pi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_teqip', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score7', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_warden', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_asst_warden', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_asso_dean', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_chairman', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_fac_inch_inst_activities', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score8', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_chairman_comm', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_fac_inch_comm', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score9', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_dept_activities', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sem_dept_comm', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score10', models.DecimalField(decimal_places=3, max_digits=6)),
                ('workshop', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score11', models.DecimalField(decimal_places=3, max_digits=6)),
                ('for2week_nat_prgm', models.DecimalField(decimal_places=3, max_digits=6)),
                ('for1week_nat_prgm', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score12', models.DecimalField(decimal_places=3, max_digits=6)),
                ('conf_as_chairman', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score13', models.DecimalField(decimal_places=3, max_digits=6)),
                ('teaching_year', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score14', models.DecimalField(decimal_places=3, max_digits=6)),
                ('labs', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score15', models.DecimalField(decimal_places=3, max_digits=6)),
                ('theory_credit_hrs', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score16', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pg', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score17', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ug', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score18', models.DecimalField(decimal_places=3, max_digits=6)),
                ('books_international', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score19', models.DecimalField(decimal_places=3, max_digits=6)),
                ('books_national', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score20', models.DecimalField(decimal_places=3, max_digits=6)),
                ('outreach_activities', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score21', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fellowship', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score22', models.DecimalField(decimal_places=3, max_digits=6)),
                ('above85', models.DecimalField(decimal_places=3, max_digits=6)),
                ('above75', models.DecimalField(decimal_places=3, max_digits=6)),
                ('score', models.DecimalField(decimal_places=3, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
