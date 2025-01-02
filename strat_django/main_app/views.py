from django.shortcuts import render, redirect
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from . models import Objective, KeyResult
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
