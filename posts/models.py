from django.db import models
from django.utils import timezone

class news(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(default = timezone.now)
    
    def  __str__(self):
        return self.title
