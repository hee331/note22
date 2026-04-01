from django.db import models

class data(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hobbies = models.CharField(max_length=100)
    gakureki = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
