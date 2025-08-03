from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from designers.forms import DesignerCreateForm, DesignerEditForm
from designers.models import Designer
# Create your views here.


class DesignerListView(LoginRequiredMixin, ListView):
    model = Designer
    template_name = 'designer/designers.html'


class DesignerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'designers.add_designer'
    model = Designer
    template_name = 'designer/designer-add.html'
    form_class = DesignerCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse(
            'designers',
        )


class DesignerDetailView(LoginRequiredMixin, DetailView):
    model = Designer
    template_name = 'designer/designer-details.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        designer = self.get_object()
        kwargs.update({'designer': designer})
        return super().get_context_data(**kwargs)


class DesignerEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'designers.change_designer'
    model = Designer
    template_name = 'designer/designer-edit.html'
    pk_url_kwarg = 'pk'
    form_class = DesignerEditForm

    def get_success_url(self) -> str:
        return reverse('designer-details', kwargs={'pk': self.object.pk})