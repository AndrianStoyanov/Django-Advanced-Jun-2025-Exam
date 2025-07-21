
from django import forms
from core.mixins import ReadOnlyFieldsMixin, ContractBaseForm
from supervisions.models import Supervision
from projects.models import Project


class SupervisionBaseForm(ContractBaseForm):
    project = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        required=False,
        label="Connect to projects",
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta(ContractBaseForm.Meta):
        model = Supervision
        fields = '__all__'


class SupervisionCreateForm(SupervisionBaseForm):
    ...


class SupervisionEditForm(SupervisionBaseForm):
    ...


class SupervisionDetailsForm(SupervisionBaseForm):
    ...


class SupervisionDeleteForm(SupervisionBaseForm, ReadOnlyFieldsMixin):
    class Meta(SupervisionBaseForm.Meta):
        model = Supervision
        exclude = ('budged', 'phone_number', 'email', 'document', 'project')