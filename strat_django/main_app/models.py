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


class Swot(models.Model):
    categorys = [
        ("Business", "Business"),
        ("Project", "Project"),
        ("Product", "Product"),
        ("Team", "Team"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="swots",)
    name = models.CharField(max_length=100)
    swot_categories = models.CharField(max_length=30, choices=categorys)

class SwotItem(models.Model):
    swot_choices = [
        ("Strengths", "Strenghts"),
        ("Weakness", "Weakness"),
        ("Opportunity", "Opportunity"),
        ("Threat", "Threat")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SwotItem", default=1)
    swots = models.ForeignKey(Swot, on_delete=models.CASCADE, related_name="items")
    item_type = models.CharField(max_length=50, choices=swot_choices)
    description = models.CharField(max_length=1000)

class MindMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mindmap", )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ideas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ideas",)
    mindmap = models.ForeignKey(MindMap, on_delete=models.CASCADE, related_name="ideas")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)


class Roadmap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roadmap",)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
