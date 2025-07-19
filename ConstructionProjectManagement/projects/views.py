from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from projects.forms import ProjectCreateForm, ProjectEditForm, ProjectDeleteForm, ProjectDetailsForm
from projects.models import Project


# Create your views here.
class CreateProjectView(CreateView):
    model = Project
    template_name = 'projects/projects-create.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.user.pk = self.request.user.pk
        form.save()
        return super().form_valid(form)


class DetailsProjectView(DetailView):
    model = Project
    form_class = ProjectDetailsForm
    template_name = 'projects/projects-details.html'
    pk_url_kwarg = 'pro_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()

        total_sum_designers = sum(designer.budget for designer in project.designers.all())
        total_sum_builders = sum(build.budget for build in project.builders.all())
        total_sum_supervisions = sum(supervision.budget for supervision in project.supervisions.all())
        total_budget_project = total_sum_designers + total_sum_builders + total_sum_supervisions
        context['total_budget_project'] = total_budget_project
        return context


class EditProjectView(UpdateView):
    model = Project
    form_class = ProjectEditForm
    template_name = 'projects/projects-edit.html'
    pk_url_kwarg = 'pro_pk'
    success_url = reverse_lazy('projects-details')


class DeleteProjectView(DeleteView):
    model = Project
    form_class = ProjectDeleteForm
    template_name = 'projects/projects-delete.html'
    pk_url_kwarg = 'pro_pk'
    success_url = reverse_lazy('projects')