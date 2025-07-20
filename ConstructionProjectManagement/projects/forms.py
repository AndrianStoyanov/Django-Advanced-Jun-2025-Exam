from django import forms

from core.mixins import ReadOnlyFieldsMixin
from projects.choices import DevelopmentChoices
from projects.models import Project


class ProjectBaseForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('user',)
        labels = {
            'title': 'Project name:',
            'code_project': 'Code project:',
            'content': 'Description:',
            'coordinator': 'Coordinator:',
            'investor': 'Investor control:',
            'date_start': 'Start project:',
            'development': 'Development Status:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter project name'}),
            'code_project': forms.TextInput(attrs={'placeholder': 'Enter code project'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter description'}),
            'coordinator': forms.TextInput(attrs={'placeholder': 'Enter coordinator'}),
            'investor': forms.TextInput(attrs={'placeholder': 'Enter investor control'}),
            'date_start': forms.DateInput(attrs={'type': 'date'}),
            'development': forms.Select(),
        }


class ProjectCreateForm(ProjectBaseForm):
    ...


class ProjectEditForm(ProjectBaseForm):
    ...


class ProjectDetailsForm(ProjectBaseForm):
    ...


class ProjectDeleteForm(ProjectBaseForm, ReadOnlyFieldsMixin):
    class Meta:
        model = Project
        exclude = ('coordinator', 'investor', 'user')
