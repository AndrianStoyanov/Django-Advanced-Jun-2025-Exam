# from django.db import models
# from projects.choices import DevelopmentChoices
#
#
# # Create your models here.
# class Project(models.Model):
#     title = models.CharField(max_length=300)
#     content = models.TextField()
#     coordinator = models.CharField(max_length=100)
#     investor = models.CharField(max_length=100)
#     date_start = models.DateField()
#     development = models.CharField(max_length=50, choices=DevelopmentChoices.choices)


# class Task(models.Model):
#     description = models.TextField()
#     author = models.CharField(
#         max_length=50,
#     )
#     date_approved = models.DateTimeField(auto_now_add=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)


# class Report(models.Model):
#     answer = models.TextField()
#     date_report = models.DateTimeField(auto_now=True)

