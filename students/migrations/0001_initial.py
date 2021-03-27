# Generated by Django 3.1.7 on 2021-03-26 20:10

import datetime
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_email', models.CharField(max_length=50)),
                ('student_phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('date_of_birth', models.DateField(blank=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('date_of_application', models.DateField(blank=True, verbose_name='applied')),
                ('date_of_acceptance', models.DateField(blank=True, verbose_name='accepted')),
                ('date_of_enrollemnt', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='enrolled')),
                ('application_essay', models.TextField(verbose_name='essay')),
                ('date_of_prep_start', models.DateField(blank=True, verbose_name='prep_start')),
                ('date_of_ses_start', models.DateField(blank=True, verbose_name='ses_start')),
                ('date_of_ma_1_start', models.DateField(blank=True, verbose_name='ma_1_start')),
                ('date_of_ma_2_start', models.DateField(blank=True, verbose_name='ma_2_start')),
                ('date_of_ma_3_start', models.DateField(blank=True, verbose_name='ma_3_start')),
                ('year_as_student', models.CharField(choices=[('APPL', 'Applicant'), ('PREP', 'PREP'), ('SES', 'SES'), ('MA_1', 'MA_1'), ('MA_2', 'MA_2'), ('MA_3', 'MA_3'), ('MA_4', 'MA_4'), ('GR', 'GR')], default='APPL', max_length=4)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
