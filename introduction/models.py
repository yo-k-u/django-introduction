from django.db import models

class Visit(models.Model):
    data=models.JSONField()