# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_food_item, name='add_food_item'),
    path('home', base_message, name='base_message'),
    path('delete/<str:restaurant>/<str:name>/', delete_food, name='delete_food'),
    path('everything', get_all_food_items, name='get_all_food_items'),
]
