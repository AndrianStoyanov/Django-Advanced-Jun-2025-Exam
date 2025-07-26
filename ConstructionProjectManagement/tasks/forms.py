from django import forms
from core.mixins import TaskBaseForm, ReadOnlyFieldsMixin, ReportBaseForm
from projects.models import Project
from tasks.models import Task, UserModel, Report


# Forms for Tasks
class TaskMainForm(TaskBaseForm):
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=False,
        label="Connect to projects",
        widget=forms.Select()
    )

    # author = forms.ModelChoiceField(
    #     queryset=UserModel.objects.all(),
    #     required=False,
    #     label="Author",
    #     widget=forms.Select()
    # )

    class Meta(TaskBaseForm.Meta):
        model = Task
        # fields = '__all__'
        exclude = ('author',)


class TaskCreateForm(TaskMainForm):
    ...


class TaskEditForm(TaskMainForm):
    ...


class TaskDetailForm(TaskMainForm):
    ...


class TaskDeleteForm(TaskMainForm, ReadOnlyFieldsMixin):
    class Meta(TaskMainForm.Meta):
        model = Task
        exclude = ('project', 'author')


# Forms for report
class ReportMainForm(ReportBaseForm):
    task = forms.ModelChoiceField(
        queryset=Task.objects.all(),
        required=False,
        label="Connect to tasks",
        widget=forms.Select()
    )
    # reporter = forms.ModelChoiceField(
    #     queryset=UserModel.objects.all(),
    #     required=False,
    #     label="Reporter",
    #     widget=forms.Select()
    # )

    class Meta(ReportBaseForm.Meta):
        model = Report
        exclude = ('reporter',)


class ReportCreateForm(ReportMainForm):
    ...


class ReportEditForm(ReportMainForm):
    ...


class ReportDetailForm(ReportMainForm):
    ...


class ReportDeleteForm(ReportMainForm, ReadOnlyFieldsMixin):
    class Meta(ReportMainForm.Meta):
        model = Report
        exclude = ('task', 'reporter',)
