from django.db import models

# Create your models here.


# class Task(models.Model):
#     description = models.TextField()
#     author = models.CharField(
#         max_length=50,
#     )
#     date_approved = models.DateTimeField(auto_now_add=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)
#
#
# class Report(models.Model):
#     answer = models.TextField()
#     date_report = models.DateTimeField(auto_now=True)