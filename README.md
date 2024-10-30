# Microservice2-Product-Service
The Product microservice is responsible for managing all product-related functionalities. It handles the creation, retrieval, updating, and deletion of food items offered by restaurants. The Product Microservice is built using Django. It operates independently with its own database and exposes a set of RESTful API endpoints for integration with the composite microservice and other sub-microservices.

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

## API Endpoints

### Base Message
- URL: ```GET /```
- Description: Returns a welcome message or basic information about the microservice.
- Input argument: None

### Add Food Item
- URL: ```POST /add_food_item/```
- Description: Creates a new food item.
- Input argument:
  | Parameter      | Type     | Description                                 |
  | -------------- | -------- | ------------------------------------------- |
  | `restaurant`   | String   | Name of the restaurant                      |
  | `name`         | String   | Name of the food item                       |
  | `price`        | Decimal  | Price of the food item (e.g., 9.99)         |
  | `calorie`      | Integer  | Calorie count of the food item              |
  | `description`  | String   | Description of the food item                |
  | `is_available` | Boolean  | Availability status (default is `true`)     |


### Get All Food Items
- URL: ```GET /everything/```
- Description: Retrieves a list of all food items.
- Input argument: None

### Get Food Items by Restaurant
- URL: ```GET /getMenu/<str:restaurant>/```
- Description: Retrieves all food items offered by a specific restaurant.
- Input argument:
  | Parameter      | Type     | Description                                 |
  | -------------- | -------- | ------------------------------------------- |
  | `restaurant`   | String   | Name of the restaurant                      |

### Delete Food Item
- URL: ```DELETE /delete/<str:restaurant>/<str:name>/```
- Description: Deletes a food item specified by the restaurant name and food item name.
- Input argument:
  | Parameter      | Type     | Description                                 |
  | -------------- | -------- | ------------------------------------------- |
  | `restaurant`   | String   | Name of the restaurant                      |
  | `name`         | String   | Name of the food item                       |
