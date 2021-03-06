"""Schools URL Configuration
"""

from django.urls import path
from . import views  
from django.views import generic

urlpatterns = [
    path('', views.index, name='index' ),
    path('schools/prep', views.prep, name='prep'),
    path('schools/ses', views.ses, name='ses'),
    path('schools/map', views.map, name='map'),
    path('schools/about', views.about, name='about'),
    path('schools/faq', views.faq, name='faq'),
]
