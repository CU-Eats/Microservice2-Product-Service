from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food
from .serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import Http404


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

router = DefaultRouter()
router.register(r'foods', FoodViewSet, basename='food')


@api_view(['GET'])
def base_message(request):
    return Response({"message": "Welcome to the Food API!"})

@csrf_exempt
@api_view(['POST'])
def add_food_item(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        # Check if food with the same name already exists in the same restaurant
        restaurant = serializer.validated_data['restaurant']
        name = serializer.validated_data['name']
        if Food.objects.filter(Q(restaurant=restaurant) & Q(name=name)).exists():
            return Response({'error': 'This food item already exists in the restaurant.'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Save the new food item
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def delete_food(request, restaurant, name):
    """
    Delete a food item by its restaurant and name.
    """
    try:
        # Try to find the food item
        food_item = Food.objects.get(restaurant=restaurant, name=name)
        food_item.delete()
        # Return a success message upon deletion
        return Response(
            {
                'message': f'Food item {name} from restaurant {restaurant} deleted successfully.'
            },
            status=status.HTTP_200_OK
        )
    except Food.DoesNotExist:
        # Return a clean and user-friendly error message
        return Response(
            {
                'error': f'Food item {name} from restaurant {restaurant} does not exist.'
            },
            status=status.HTTP_404_NOT_FOUND
        )

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
