from django.contrib.auth import get_user_model
from django.db import models
from projects.choices import DevelopmentChoices
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

UserModel = get_user_model()


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300)
    code_project = models.CharField(max_length=10, validators=[MinLengthValidator(5)], default=00000)
    content = models.TextField()
    coordinator = models.CharField(max_length=30)
    investor = models.CharField(max_length=30)
    date_start = models.DateField(blank=True, null=True)
    development = models.CharField(max_length=50, choices=DevelopmentChoices.choices)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE, related_name='created_by'
    )

    def __str__(self):
        return self.title


