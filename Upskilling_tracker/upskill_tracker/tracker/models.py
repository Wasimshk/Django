from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    date = models.DateField()
    progress = models.TextField()

    def __str__(self):
        return f"{self.goal.title} - {self.date}"

