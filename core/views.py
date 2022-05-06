#PACKAGES
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
#LOCAL
from .models import Blank
from .forms import BlankCreateForm


#Super class Tree
#Super class Tree
class SuperCL(CreateView, ListView):
    pass

class SuperUD(UpdateView, DeleteView):
    pass

class Super(SuperCL, SuperUD):
    pass
#Super class Tree
#Super class Tree

class BlankView(SuperCL):
    model = Blank
    template_name = "main.html"
    form_class = BlankCreateForm
    context_object_name = "list_blank"
    success_url = reverse_lazy('main')
    def get_context_data(self, **kwargs):
        kwargs['bc'] = Blank.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)