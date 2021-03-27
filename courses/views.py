# COURSES VIEW
from django.shortcuts import render, get_object_or_404
from courses.models import Course
from django.views import generic
from django.views.generic import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.decorators import login_required, permission_required # for function view decorator
# import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# from django.views.generic.edit import CreateView, UpdateView, DeleteView

# def index(request):
#     return render(request, 'courses/index.html')



class CourseList(ListView):

    queryset = Course.objects.order_by('course_name')
    context_object_name = 'course_list'


class CourseDetail(generic.DetailView):
    model = Course
    context_object_name = 'course'

