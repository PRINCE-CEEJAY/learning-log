from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    picture_url = models.CharField()

    class Meta:
        unique_together = ('username', 'email', 'password')

    def __str__(self):
        return self.username