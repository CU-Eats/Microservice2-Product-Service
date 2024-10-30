# Microservice2-Product-Service

## Features
- **Stores and retrieves restaurant information and menu data**
- **Enables menu updates and modifications by restaurant owners**

## Food Model
The food data is stored using the following Django model:
```
from django.db import models

class Food(models.Model):
    restaurant = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calorie = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

def __str__(self):
    return f"{self.name} - {self.restaurant}"
```
