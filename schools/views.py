# SCHOOLS VIEW

from django.shortcuts import render, get_object_or_404
# from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.decorators import login_required, permission_required # for function view decorator
# import datetime
from django.http import HttpResponseRedirect
# from django.urls import reverse, reverse_lazy
# from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'schools/index.html')
