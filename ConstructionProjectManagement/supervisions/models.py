from django.db import models
from core.mixins import AbstractBaseMixin
from core.validators import SizeValidator

# Create your models here.


class Supervision(AbstractBaseMixin):
    document = models.FileField(
        validators=[
            SizeValidator(5),
        ],
        upload_to='supervision_documents',
    )
    project = models.ManyToManyField('projects.Project', related_name='supervisions')
