from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # quand l'user est créé, on utilise cette méthode pour le loguer

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# def task_list(request):
#     return HttpResponse('teest')

class CustomLogin(LoginView):
    template_name = 'base/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        # si on veut accerder a cette class en étant logué on est redirigé vers l'accueil
        if self.request.user.is_authenticated: 
            return redirect('task-list')
        return super().get(*args, **kwargs)
    

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # je récupère tous les objets du models Task et je filtre avec l'utilisateur logué
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        #  je peux ajouter des champs au context en plus des champs du model Task
        context['counter'] = context['tasks'].count()
        return context
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete'] # On précise les champs pour ne pas pouvoir choisir l'utilisateur en front
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        # modification du formulaire pour que l'utilisateur soit préremplie
        form.instance.user = self.request.user
        return super().form_valid(form)



class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task-list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
