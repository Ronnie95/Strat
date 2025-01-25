from django.shortcuts import render, redirect
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from . models import Objective, KeyResult, Swot, SwotItem, MindMap, Ideas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.urls import reverse
from django.views import View # <- View class to handle requests
from django.views.generic import ListView
from .forms import UploadFileForm



# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

@method_decorator(login_required, name='dispatch')
class Roadmap(TemplateView):
    template_name = "roadmaps.html"



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
    
#@method_decorator(login_required, name='dispatch')
#class KeyResultList(TemplateView):
 #   template_name = "keyresults.html"

  #  def get_context_data(self, **kwargs):
  #      context = super().get_context_data(**kwargs)
  #      context["KeyResult"] = KeyResult.objects.all() # Here we are using the model to query the database for us.
   #     return context
    
@method_decorator(login_required, name='dispatch')
class KeyResultList(ListView):
    model = KeyResult
    template_name = "keyresults.html"
    context_object_name = "key_results"  # Rename for clarity

    def get_queryset(self):
        # Return only the key results for the logged-in user
        return KeyResult.objects.filter(user=self.request.user)
    
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


@method_decorator(login_required, name='dispatch')
class SwotCreate(CreateView):
    model = Swot
    fields = ['name', 'swot_categories']
    template_name = "swots_create.html"
    success_url = "/swots/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SwotCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('swots_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class SwotList(TemplateView):
    template_name = "swots.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Swot"] = Swot.objects.all() # Here we are using the model to query the database for us.
        return context
    

@method_decorator(login_required, name='dispatch')
class SwotDetail(DetailView):
    model = Swot
    template_name = "swots_detail.html"
    context_object_name = 'swot'

    
    def get_queryset(self):
        return Swot.objects.filter(user=self.request.user)
    
class SwotUpdate(UpdateView):
    model = Swot
    fields = ['name', 'swot_categories']
    template_name = "swots_update.html"
    success_url = "/swots/"

class SwotDelete(DeleteView):
    model = Swot
    template_name = "swots_delete.html"
    success_url = "/swots/"

@method_decorator(login_required, name='dispatch')
class SwotItemCreate(CreateView):
    model = SwotItem
    fields = ['swots', 'item_type', "description"]
    template_name = "swotitem_create.html"
    success_url = "/swotitems/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SwotItemCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('swotitem_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class SwotItemList(ListView):
    model = SwotItem
    template_name = "swotitems.html"
    context_object_name = "key_results"  # Rename for clarity

    def get_queryset(self):
        # Return only the key results for the logged-in user
        return SwotItem.objects.filter(user=self.request.user)
    
@method_decorator(login_required, name='dispatch')
class SwotItemDetail(DetailView):
    model = SwotItem
    template_name = "swotitem_detail.html"
    
    def get_queryset(self):
        return SwotItem.objects.filter(user=self.request.user)
    
class SwotItemUpdate(UpdateView):
    model = SwotItem
    fields = ['swots', 'item_type', 'description']
    template_name = "swotitem_update.html"
    success_url = "/swotitems/"

class SwotItemDelete(DeleteView):
    model = SwotItem
    template_name = "swotitem_delete.html"
    success_url = "/swotitems/"
 ##may have to have the success URL be to objectives due to the one to many relationship

@method_decorator(login_required, name='dispatch')
class MindMapCreate(CreateView):
    model = MindMap
    fields = ['name', 'description']
    template_name = "mindmap_create.html"
    success_url = "/mindmaps/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MindMapCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('mindmap_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class MindMapList(TemplateView):
    template_name = "mindmaps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["MindMap"] = MindMap.objects.all() # Here we are using the model to query the database for us.
        return context
    

@method_decorator(login_required, name='dispatch')
class MindMapDetail(DetailView):
    model = MindMap
    template_name = "mindmap_detail.html"
    context_object_name = 'mindmap'

    
    def get_queryset(self):
        return MindMap.objects.filter(user=self.request.user)
    
class MindMapUpdate(UpdateView):
    model = MindMap
    fields = ['name', 'description']
    template_name = "mindmap_update.html"
    success_url = "/mindmaps/"

class MindMapDelete(DeleteView):
    model = MindMap
    template_name = "mindmap_delete.html"
    success_url = "/mindmaps/"


@method_decorator(login_required, name='dispatch')
class IdeaCreate(CreateView):
    model = Ideas
    fields = ['mindmap', 'title', "description"]
    template_name = "idea_create.html"
    success_url = "/mindmaps/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IdeaCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('idea_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class IdeaList(ListView):
    model = Ideas
    template_name = "ideas.html"
    context_object_name = "mindmaps"  # Rename for clarity

    def get_queryset(self):
        # Return only the key results for the logged-in user
        return Ideas.objects.filter(user=self.request.user)
    
@method_decorator(login_required, name='dispatch')
class IdeaDetail(DetailView):
    model = Ideas
    template_name = "idea_detail.html"
    
    def get_queryset(self):
        return Ideas.objects.filter(user=self.request.user)
    
class IdeaUpdate(UpdateView):
    model = Ideas
    fields = ['mindmap', 'title', 'description']
    template_name = "idea_update.html"
    success_url = "/ideas/"

class IdeaDelete(DeleteView):
    model = Ideas
    template_name = "idea_delete.html"
    success_url = "/ideas/"
 ##may have to have the success URL be to objectives due to the one to many relationship


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            roadmap = form.save(commit=False)
            roadmap.user = request.user  # Assign the current user
            roadmap.save()
            return redirect('success')  # Replace with your success page or URL name
    else:
        form = UploadFileForm()
    return render(request, 'roadmaps.html', {'form': form})