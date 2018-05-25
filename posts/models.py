from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(default = timezone.now)
    
    def  __str__(self):
        return (self.title)

class Key(models.Model):
    key = models.CharField(max_length=255)
    def __str__(self): 
     return self.key

