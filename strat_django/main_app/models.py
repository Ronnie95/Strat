from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Objectives(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category_Choices = (
        ("Not started", "Not started"),
        ("In Progress", "In Progress"),
        ("On Hold", "On Hold"),
        ("Complete", "Complete"),
    )
    progress = models.CharField(max_length=30, choices=category_Choices, default="not started")