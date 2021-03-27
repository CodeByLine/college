"""Courses URL Configuration
"""

from django.urls import path
from . import views  
from django.views import generic


urlpatterns = [
    # path('', views.index, name='index' ),
    path('', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>', views.CourseDetail.as_view(), name='course-detail'),
]
