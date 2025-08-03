from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from builders.forms import BuilderEditForm, BuilderCreateForm
from builders.models import Builder


# Create your views here.
class BuilderListView(LoginRequiredMixin, ListView):
    model = Builder
    template_name = 'builder/builders.html'


class BuilderCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "builders.add_builder"
    model = Builder
    template_name = 'builder/builder-add.html'
    form_class = BuilderCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse(
            'builders',
        )


class BuilderDetailView(LoginRequiredMixin, DetailView):
    model = Builder
    template_name = 'builder/builder-details.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        builder = self.get_object()
        kwargs.update({'builder': builder})
        return super().get_context_data(**kwargs)


class BuilderEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'builders.edit_builder'
    model = Builder
    form_class = BuilderEditForm
    template_name = 'builder/builder-edit.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self) -> str:
        return reverse('builder-details', kwargs={'pk': self.object.pk})

