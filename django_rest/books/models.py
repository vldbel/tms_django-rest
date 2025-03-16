from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=False, null=False)
    published_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


# class Author(models.Model):
#     first_name = models.CharField(max_length=100)  # it should be 100
#     last_name = models.CharField(max_length=100) 
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('Died', null=True, blank=True)

#     # def get_absolute_url(self):
#     #     return reverse('author-detail', args=[str(self.id)])

#     def __str__(self):
#         return f'{self.last_name}, {self.first_name}'
