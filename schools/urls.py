"""Schools URL Configuration
"""

from django.urls import path
from . import views  
from django.views import generic

urlpatterns = [
    path('', views.index, name='index' ),
]
