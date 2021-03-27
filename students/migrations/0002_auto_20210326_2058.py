# Generated by Django 3.1.7 on 2021-03-27 01:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='plantostart',
            field=models.DateField(default=datetime.datetime.now, verbose_name='plantostart'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_acceptance',
            field=models.DateField(verbose_name='accepted'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_application',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='applied'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_enrollemnt',
            field=models.DateField(verbose_name='enrolled'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_ma_1_start',
            field=models.DateField(verbose_name='ma_1_start'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_ma_2_start',
            field=models.DateField(verbose_name='ma_2_start'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_ma_3_start',
            field=models.DateField(verbose_name='ma_3_start'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_prep_start',
            field=models.DateField(verbose_name='prep_start'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_ses_start',
            field=models.DateField(verbose_name='ses_start'),
        ),
    ]
