from django.db import models
from core.mixins import AbstractBaseMixin
from core.validators import SizeValidator

# Create your models here.


class Designer(AbstractBaseMixin):
    document = models.FileField(
        validators=[
            SizeValidator(5),
        ],
        upload_to='designer_documents',
    )
    project = models.ManyToManyField('projects.Project', related_name='designers')