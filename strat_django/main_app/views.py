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

@method_decorator(login_required, name='dispatch')
class ObjectiveCreate(CreateView):
    model = Objective
    fields = ['title', 'description', 'start_date', 'end_date', 'progress']
    template_name = "objective_create.html"
    success_url = "/objectives/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ObjectiveCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('goal_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class ObjectiveList(TemplateView):
    template_name = "objectives.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Goals"] = Goals.objects.all() # Here we are using the model to query the database for us.
        return context
    

@method_decorator(login_required, name='dispatch')
class GoalDetail(DetailView):
    model = Goals
    template_name = "goal_detail.html"
    
    def get_queryset(self):
        return Goals.objects.filter(user=self.request.user)
    
class GoalUpdate(UpdateView):
    model = Goals
    fields = ['goal_name', 'target_amount', 'target_date', 'notes']
    template_name = "goal_update.html"
    success_url = "/goal/"

class GoalDelete(DeleteView):
    model = Goals
    template_name = "goal_delete.html"
    success_url = "/goal/"