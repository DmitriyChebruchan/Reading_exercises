from django.db import models

class UserInput(models.Model):
    text = models.TextField()
    speed = models.IntegerField()
