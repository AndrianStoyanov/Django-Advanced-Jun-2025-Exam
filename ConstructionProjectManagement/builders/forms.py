from django import forms

from builders.models import Builder
from core.mixins import ReadOnlyFieldsMixin, ContractBaseForm
from projects.models import Project


class BuilderBaseForm(ContractBaseForm):
    project = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        required=False,
        label="Connect to projects",
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta(ContractBaseForm.Meta):
        model = Builder
        fields = '__all__'


class BuilderCreateForm(BuilderBaseForm):
    ...


class BuilderEditForm(BuilderBaseForm):
    ...


class BuilderDetailsForm(BuilderBaseForm):
    ...


class BuilderDeleteForm(BuilderBaseForm, ReadOnlyFieldsMixin):
    class Meta(BuilderBaseForm.Meta):
        model = Builder
        exclude = ('budged', 'phone_number', 'email', 'document', 'project')
