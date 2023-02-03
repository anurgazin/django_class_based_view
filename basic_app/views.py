from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['inject_me'] = 'basic injection'
    #     return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')

class StudentCreateView(CreateView):
    fields = ('name', 'age', 'school')
    model = models.Student

class StudentUpdateView(UpdateView):
    fields=('name', 'school')
    model = models.Student

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('basic_app:list')