from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from tasks.forms import TaskCreateForm, ReportCreateForm, ReportEditForm, TaskEditForm, TaskDeleteForm, ReportDeleteForm
from tasks.models import Task, Report


# Create your views here.
# Views for Tasks
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/tasks-create.html'
    form_class = TaskCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/tasks-details.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        task = self.get_object()
        kwargs.update({'task': task})
        return super().get_context_data(**kwargs)


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/tasks-edit.html'
    pk_url_kwarg = 'pk'
    form_class = TaskEditForm

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/tasks-delete.html'
    pk_url_kwarg = 'pk'
    form_class = TaskDeleteForm
    success_url = reverse_lazy('tasks')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"data": self.get_initial()})
        return kwargs


# Views for Reports
# class ReportListView(ListView):
#     model = Report
#     template_name = 'tasks/reports.html'


# class ReportCreateView(LoginRequiredMixin, CreateView):
#     model = Report
#     template_name = 'tasks/report-create.html'
#     form_class = ReportCreateForm
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.reporter = self.request.user
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('tasks')
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'tasks/report-create.html'
    form_class = ReportCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.reporter = self.request.user
        task_id = self.request.GET.get('task_id')
        if task_id:
            from tasks.models import Task
            try:
                task = Task.objects.get(pk=task_id)
                self.object.task = task
            except Task.DoesNotExist:
                pass

        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.task.pk})


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'tasks/report-detail.html'
    pk_url_kwarg = 'rep_pk'

    def get_context_data(self, **kwargs):
        report = self.get_object()
        kwargs.update({'report': report})
        return super().get_context_data(**kwargs)


class ReportEditView(LoginRequiredMixin, UpdateView):
    model = Report
    template_name = 'tasks/report-edit.html'
    pk_url_kwarg = 'rep_pk'
    form_class = ReportEditForm

    def get_success_url(self):
        return reverse('report-detail', kwargs={'rep_pk': self.object.pk})


class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'tasks/report-delete.html'
    pk_url_kwarg = 'rep_pk'
    form_class = ReportDeleteForm

    def get_initial(self) -> dict:
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"data": self.get_initial()})
        return kwargs

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.task.pk})

