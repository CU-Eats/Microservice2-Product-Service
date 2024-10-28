from django.shortcuts import render, HttpResponse
from .models import foods
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from rest_framework import status


@api_view(['GET'])
def getData(request):
    items = foods.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# Create your views here.
def home(request):
    return render(request,"home.html")

def food(request):
    foods = foods.objects.all()
    return render(request,"food.html",{"foods":foods})


@api_view(['POST'])
def addItem(request,name):
    # Expecting a single string input in the format: "name-description-price"
    input_string = name
    # Split the string into three parts
    try:
        name, description, price = input_string.split('-')

        # Prepare data as JSON for the serializer
        item_data = {
            'name': name.strip(),
            'description': description.strip(),
            'price': float(price.strip())  # Convert price to float
        }

        # Use the serializer to validate and save the data
        serializer = ItemSerializer(data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        # If there aren't exactly three parts in the input string, return an error
        return Response({'error': 'Invalid input format. Expected "name-description-price".'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteItemByName(request, name):
    try:
        # Try to get the item by its name (case-sensitive)
        item = foods.objects.get(name=name)
        item.delete()  # Delete the item from the database
        return Response({'message': f'Item "{name}" was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    except Item.DoesNotExist:
        return Response({'error': f'Item with name "{name}" not found'}, status=status.HTTP_404_NOT_FOUND)