from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer


@api_view(['GET', 'POST'])
def item_list(request):
    """
    List all items or create a new item.

    GET:
    Returns a list of all items.

    POST:
    Creates a new item based on request data.
    """
    if request.method == 'GET':
        # Retrieve all items from the database
        items = Item.objects.all()
        # Serialize the queryset of items
        serializer = ItemSerializer(items, many=True)
        # Return serialized data as a JSON response
        return Response(serializer.data)

    elif request.method == 'POST':
        # Deserialize request data into an ItemSerializer instance
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid serializer data to the database
            serializer.save()
            # Return serialized data of the newly 
            # created item with 201 Created status
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        # Return errors if serializer data is not 
        # valid with 400 Bad Request status
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    """
    Retrieve, update or delete an item.

    GET:
    Retrieve details of a specific item.

    PUT:
    Update details of a specific item based on request data.

    DELETE:
    Delete a specific item.
    """
    try:
        # Attempt to retrieve the item with the given primary key
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        # Return 404 Not Found if item with pk does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize and return the details 
        # of the retrieved item
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Deserialize request data into an ItemSerializer 
        # instance with current item instance
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            # Save the valid serializer data to update the item
            serializer.save()
            # Return serialized data of the updated item
            return Response(serializer.data)
        # Return errors if serializer data is not 
        # valid with 400 Bad Request status
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the item from the database
        item.delete()
        # Return 204 No Content to indicate 
        # successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
