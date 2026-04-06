from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lesson(models.Model):
    topic = models.CharField(max_length=100)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic
