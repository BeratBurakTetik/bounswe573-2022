from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    creationTime = models.DateField()
