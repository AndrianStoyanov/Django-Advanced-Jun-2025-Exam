from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from supervisions.forms import SupervisionCreateForm, SupervisionEditForm
from supervisions.models import Supervision


# Create your views here.
class SupervisionListView(LoginRequiredMixin, ListView):
    model = Supervision
    template_name = 'supervision/supervisions.html'


class SupervisionCreateView(LoginRequiredMixin, CreateView):
    model = Supervision
    template_name = 'supervision/supervision-add.html'
    form_class = SupervisionCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse(
            'supervisions',
        )


class SupervisionDetailView(LoginRequiredMixin, DetailView):
    model = Supervision
    template_name = 'supervision/supervision-details.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        supervision = self.get_object()
        kwargs.update({'supervision': supervision})
        return super().get_context_data(**kwargs)


class SupervisionEditView(LoginRequiredMixin, UpdateView):
    model = Supervision
    template_name = 'supervision/supervision-edit.html'
    pk_url_kwarg = 'pk'
    form_class = SupervisionEditForm

    def get_success_url(self) -> str:
        return reverse('supervision-details', kwargs={'pk': self.object.pk})