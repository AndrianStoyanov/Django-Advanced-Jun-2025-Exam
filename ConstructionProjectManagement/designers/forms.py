
from django import forms
from core.mixins import ReadOnlyFieldsMixin, ContractBaseForm
from designers.models import Designer
from projects.models import Project


class DesignerBaseForm(ContractBaseForm):
    project = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        required=False,
        label="Connect to projects",
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta(ContractBaseForm.Meta):
        model = Designer
        fields = '__all__'


class DesignerCreateForm(DesignerBaseForm):
    ...


class DesignerEditForm(DesignerBaseForm):
    ...


class DesignerDetailsForm(DesignerBaseForm):
    ...


class DesignerDeleteForm(DesignerBaseForm, ReadOnlyFieldsMixin):
    class Meta(DesignerBaseForm.Meta):
        model = Designer
        exclude = ('budged', 'phone_number', 'email', 'document', 'project')
