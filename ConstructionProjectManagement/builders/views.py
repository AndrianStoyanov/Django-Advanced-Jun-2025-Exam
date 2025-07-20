from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from builders.forms import BuilderBaseForm, BuilderEditForm, BuilderCreateForm
from builders.models import Builder


# Create your views here.
class BuilderListView(ListView):
    model = Builder
    template_name = 'builder/builders.html'


class BuilderCreateView(LoginRequiredMixin, CreateView):
    model = Builder
    template_name = 'builder/builder-add.html'
    form_class = BuilderCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse(
            'builders',
        )


class BuilderDetailView(DetailView):
    model = Builder
    template_name = 'builder/builder-details.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        builder = self.get_object()
        kwargs.update({'builder': builder})
        return super().get_context_data(**kwargs)


class BuilderEditView(LoginRequiredMixin, UpdateView):
    model = Builder
    template_name = 'builder/builder-edit.html'
    pk_url_kwarg = 'pk'
    form_class = BuilderEditForm

    def get_success_url(self) -> str:
        return reverse('builder-details', kwargs={'pk': self.object.pk})

