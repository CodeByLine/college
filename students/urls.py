"""Students URL Configuration
"""

from django.urls import path
from . import views  
from django.views import generic

urlpatterns = [
    path('', views.students, name='students' ),
]