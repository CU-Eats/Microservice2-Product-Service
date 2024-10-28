from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("food/",views.food,name="Food"),
    path("getData",views.getData,name="getData"),
    path('addItem/<str:name>/', views.addItem, name='addItem'),
    path('deleteItemByName/<str:name>/', views.deleteItemByName, name='deleteItemByName'),  # URL for deleting an item by name
]