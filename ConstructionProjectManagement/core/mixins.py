from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models
from django import forms
from core.validators import validator_phone, validate_name


class ReadOnlyFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
            field.widget.attrs["readonly"] = True


class AbstractBaseMixin(models.Model):
    company_name = models.CharField(max_length=110, validators=[MinLengthValidator(2), validate_name], unique=True)
    permit = models.CharField(max_length=30)
    contract = models.CharField(max_length=30)
    budged = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15, validators=[validator_phone], unique=True)
    email = models.EmailField(validators=[EmailValidator()], unique=True)

    def __str__(self):
        return self.company_name

    class Meta:
        abstract = True


class ContractBaseForm(forms.ModelForm):
    class Meta:
        labels = {
            'company_name': 'Company name:',
            'permit': 'Permit:',
            'contract': 'Contract:',
            'budged': 'Budget:',
            'phone_number': 'Phone Number:',
            'email': 'Email:',
            'document': 'Document upload:',
        }
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter company name'}),
            'permit': forms.TextInput(attrs={'placeholder': 'Enter permit number'}),
            'contract': forms.Textarea(attrs={'placeholder': 'Enter contract number'}),
            'budged': forms.NumberInput(attrs={'placeholder': 'Enter budget by euro'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number start with +359'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'document': forms.FileInput(),
        }


class TaskBaseForm(forms.ModelForm):
    class Meta:
        labels = {
            'description': 'Description:',
            'date_approved': 'Date approved:',
        }
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
            'date_approved': forms.DateTimeInput(),
        }


class ReportBaseForm(forms.ModelForm):
    class Meta:
        labels = {
            'answer': 'Answer:',
            'date_report': 'Date reported:',
        }
        widgets = {
            'answer': forms.Textarea(attrs={'placeholder': 'Enter answer'}),
            'date_report': forms.DateTimeInput(),
        }