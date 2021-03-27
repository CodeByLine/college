from django.db import models
# from django import datetime


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_number = models.CharField(max_length=100, null=True, blank=True)
    course_start_date = models.DateField('course_start_date', null=True, blank=True)
    course_end_date = models.DateField('course_end_date', null=True, blank=True)

    class Meta:
        ordering = ['course_name']

    def get_absolute_url(self):     
        # pass  
        return reverse('course-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.course_name}, {self.course_number}, {self.course_start_date}, {self.course_end_date}' 

        