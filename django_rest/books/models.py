from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=False, null=False)
    published_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
