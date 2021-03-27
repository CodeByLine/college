from django.db import models
from datetime import datetime
from phone_field import PhoneField #installed apps 'phone_field'
# from django.contrib.auth.models import User

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    student_email = models.CharField(max_length=50)
    student_phone = PhoneField(blank=False, help_text='Contact phone number')
    date_of_birth = models.DateField(blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    date_of_application = models.DateField('applied', default=datetime.now, blank=True)
    plantostart = models.DateField('plantostart', default=datetime.now, blank=True)
    date_of_acceptance = models.DateField('accepted', blank=True)
    date_of_enrollemnt = models.DateField('enrolled', blank=True)
    application_essay = models.TextField('essay')

    date_of_prep_start = models.DateField('prep_start', blank=True)
    date_of_ses_start = models.DateField('ses_start', blank=True)
    date_of_ma_1_start = models.DateField('ma_1_start', blank=True)
    date_of_ma_2_start = models.DateField('ma_2_start', blank=True)
    date_of_ma_3_start = models.DateField('ma_3_start', blank=True)

    APPLICANT = 'APPL'
    PREP = 'PREP'
    SES = 'SES'
    MA_1 = 'MA_1'
    MA_2 = 'MA_2'
    MA_3 = 'MA_3'
    MA_4 = 'MA_4'
    GRADUATE = 'GR'

    YEAR_AS_STUDENT_CHOICES = [
        (APPLICANT, 'Applicant'),
        (PREP, 'PREP'),
        (SES, 'SES'),
        (MA_1, 'MA_1'),
        (MA_2, 'MA_2'),
        (MA_3, 'MA_3'),
        (MA_4, 'MA_4'),
        (GRADUATE, 'GR')
    ]
    year_as_student = models.CharField(
        max_length=4,
        choices=YEAR_AS_STUDENT_CHOICES,
        default=APPLICANT,
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        pass   
        # return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
