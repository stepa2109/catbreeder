from django.contrib.auth.models import User
from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed_type = models.CharField(max_length=100)
    is_fluffy = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cats')

    def __str__(self):
        return f'{self.name} ({self.breed_type})'


