from django.db import models

# Create your models here.
class attendance(models.Model):
    personid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

