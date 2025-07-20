from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView

from projects.forms import ProjectCreateForm, ProjectEditForm, ProjectDeleteForm, ProjectDetailsForm
from projects.models import Project


# Create your views here.


class ProjectPageView(ListView):
    model = Project
    template_name = 'projects/projects-page.html'


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/projects-create.html'
    form_class = ProjectCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse(
            'projects',
        )


class DetailsProjectView(DetailView):
    model = Project
    template_name = 'projects/projects-details.html'
    pk_url_kwarg = 'pro_pk'

    def get_context_data(self, **kwargs):
        project = self.get_object()
        total_sum_designers = sum([designer.budged for designer in project.designers.all()]) or 0
        total_sum_builders = sum([build.budged for build in project.builders.all()]) or 0
        total_sum_supervisions = sum([supervision.budged for supervision in project.supervisions.all()]) or 0
        total_budget_project = total_sum_designers + total_sum_builders + total_sum_supervisions

        kwargs.update({
            "total_budget_project": total_budget_project,
            "project": project,
        })
        return super().get_context_data(**kwargs)


class EditProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectEditForm
    template_name = 'projects/projects-edit.html'
    pk_url_kwarg = 'pro_pk'

    def get_success_url(self) -> str:
        return reverse(
            'project-details', kwargs={'pro_pk': self.object.pk}
        )


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = Project
    form_class = ProjectDeleteForm
    template_name = 'projects/projects-delete.html'
    pk_url_kwarg = 'pro_pk'
    success_url = reverse_lazy('projects')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"data": self.get_initial()})
        return kwargs