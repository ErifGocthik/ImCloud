from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from cloudapp.models import Image


class MainListView(ListView):
    model = Image
    template_name = 'main.html'
    context_object_name = 'images'