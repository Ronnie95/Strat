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
from django.views import View # <- View class to handle requests


# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"


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
        return reverse('objective_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class ObjectiveList(TemplateView):
    template_name = "objectives.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Objective"] = Objective.objects.all() # Here we are using the model to query the database for us.
        return context
    

@method_decorator(login_required, name='dispatch')
class ObjectiveDetail(DetailView):
    model = Objective
    template_name = "objective_detail.html"
    context_object_name = 'objective'

    
    def get_queryset(self):
        return Objective.objects.filter(user=self.request.user)
    
class ObjectiveUpdate(UpdateView):
    model = Objective
    fields = ['title', 'description', 'start_date', 'end_date', 'progress']
    template_name = "objective_update.html"
    success_url = "/objectives/"

class ObjectiveDelete(DeleteView):
    model = Objective
    template_name = "objective_delete.html"
    success_url = "/objectives/"

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


@method_decorator(login_required, name='dispatch')
class KeyResultCreate(CreateView):
    model = KeyResult
    fields = ['objective', 'description', 'target_value', 'current_value', 'deadline']
    template_name = "keyresult_create.html"
    success_url = "/keyresult/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(KeyResultCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('keyresult_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class KeyResultList(TemplateView):
    template_name = "keyresults.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["KeyResult"] = Objective.objects.all() # Here we are using the model to query the database for us.
        return context
    

@method_decorator(login_required, name='dispatch')
class KeyResultDetail(DetailView):
    model = KeyResult
    template_name = "keyresult_detail.html"
    
    def get_queryset(self):
        return KeyResult.objects.filter(user=self.request.user)
    
class KeyResultUpdate(UpdateView):
    model = KeyResult
    fields = ['objective', 'description', 'target_value', 'current_value', 'deadline']
    template_name = "keyresult_update.html"
    success_url = "/keyresults/"

class KeyResultDelete(DeleteView):
    model = KeyResult
    template_name = "objective_delete.html"
    success_url = "/keyresults/"
 ##may have to have the success URL be to objectives due to the one to many relationship