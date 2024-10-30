from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food
from .serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

router = DefaultRouter()
router.register(r'foods', FoodViewSet, basename='food')


@api_view(['GET'])
def base_message(request):
    return Response({"message": "Welcome to the Food API!"})

@api_view(['POST'])
def add_food_item(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_food(request, restaurant, name):
    """
    Delete a food item by its restaurant and name.
    """
    try:
        food_item = Food.objects.get(restaurant=restaurant, name=name)
    except Food.DoesNotExist:
        raise Http404
    food_item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_food_items(request):
    """
    Get all food items from the database.
    """
    all_food_items = Food.objects.all()
    serializer = FoodSerializer(all_food_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_food_items_by_restaurant(request, restaurant):
    """
    Get all food items for a specific restaurant.
    """
    food_items = Food.objects.filter(restaurant=restaurant)
    serializer = FoodSerializer(food_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)