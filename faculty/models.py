from django.db import models
from datetime import datetime
from phone_field import PhoneField #installed apps 'phone_field'
from django.contrib.auth.models import User


class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    faculty_email = models.CharField(max_length=50)
    faculty_phone = PhoneField(blank=False, help_text='Contact phone number')
    date_of_birth = models.DateField(blank=True, help_text='optional')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    start_date = models.DateField('start_date', blank=True)
    
    graduated_date = models.DateField('graduated_date', blank=True)
    

    BOARD = 'BD'
    MENTOR = 'MT'
    TUTOR = 'TT'
    SCHOLARCH = 'SC'
    STAFF = 'ST'

    FACULTY_POSITION = [
        (BOARD, 'Board'),
        (MENTOR, 'Mentor'),
        (TUTOR, 'Tutor'),
        (SCHOLARCH, 'Scholarch'),
        (STAFF, 'Staff')
    ]

    faculty_position = models.CharField(
        max_length=2,
        choices=FACULTY_POSITION,
        default=TUTOR,
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name_plural = "faculty"

    def get_absolute_url(self):
        pass     
        # return reverse('faculty-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'