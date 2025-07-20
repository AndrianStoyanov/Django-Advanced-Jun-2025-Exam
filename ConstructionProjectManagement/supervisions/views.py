from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from supervisions.models import Supervision


# Create your views here.
class SupervisionListView(ListView):
    model = Supervision
    template_name = 'supervision/supervisions.html'


class SupervisionCreateView(LoginRequiredMixin, CreateView):
    model = Supervision
    template_name = 'supervision/supervision-add.html'


class SupervisionDetailView(DetailView):
    model = Supervision
    template_name = 'supervision/supervision-details.html'


class SupervisionEditView(LoginRequiredMixin, UpdateView):
    model = Supervision
    template_name = 'supervision/supervision-edit.html'