from django.contrib.auth import get_user_model
from django.db import models
from projects.models import Project


# Create your models here.

UserModel = get_user_model()


class Task(models.Model):
    description = models.TextField()
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    date_approved = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.project.title


class Report(models.Model):
    answer = models.TextField()
    date_report = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reports')