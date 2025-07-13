from django.contrib.auth import get_user_model
from django.db import models
from projects.choices import DevelopmentChoices
from django.core.validators import MaxValueValidator, MinValueValidator

UserModel = get_user_model()


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300)
    code_project = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(10)], default=0)
    content = models.TextField()
    coordinator = models.CharField(max_length=30)
    investor = models.CharField(max_length=30)
    date_start = models.DateField(blank=True, null=True)
    development = models.CharField(max_length=50, choices=DevelopmentChoices.choices)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE, related_name='created_by'
    )



