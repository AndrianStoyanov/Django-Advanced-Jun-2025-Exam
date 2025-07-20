from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from designers.models import Designer
from projects.models import Project


# Create your views here.


class HomeView(TemplateView):
    template_name = 'common/home.html'


class HomeExView(TemplateView):
    template_name = 'common/home-ex.html'

