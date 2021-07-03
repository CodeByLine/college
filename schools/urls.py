"""Schools URL Configuration
"""

from django.urls import path
from . import views  
from django.views import generic

urlpatterns = [
    path('', views.index, name='index' ),
    path('schools/prep', views.prep, name='prep'),
    path('schools/ses', views.ses, name='ses'),
    path('schools/mas', views.mas, name='mas'),
    path('schools/about', views.about, name='about'),
]
