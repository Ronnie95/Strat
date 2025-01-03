from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Objective(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(default="2025-01-01")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category_Choices = (
        ("Not started", "Not started"),
        ("In Progress", "In Progress"),
        ("On Hold", "On Hold"),
        ("Complete", "Complete"),
    )
    progress = models.CharField(max_length=30, choices=category_Choices, default="not started")

    def __str__(self):
        return self.title

class KeyResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="keyresults",)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name="keyresults")
    description = models.CharField(max_length=250)
    target_value = models.FloatField()
    current_value = models.FloatField()
    deadline = models.DateField()

    def __str__(self):
        return self.description

