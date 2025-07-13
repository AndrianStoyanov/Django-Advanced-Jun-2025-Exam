from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models

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

    class Meta:
        abstract = True
