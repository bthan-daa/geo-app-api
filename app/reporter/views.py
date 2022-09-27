from django.shortcuts import render  # noqa
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Park, Incidence

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'
