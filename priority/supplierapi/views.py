from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Supplier
from .serializers import SupplierSerializer


@api_view(['GET', 'POST'])
def supplier_list(request):
    """
    List all suppliers or create a new supplier.

    GET:
    Returns a list of all suppliers.

    POST:
    Creates a new supplier based on request data.
    """
    if request.method == 'GET':
        # Retrieve all suppliers from the database
        suppliers = Supplier.objects.all()
        # Serialize the queryset of suppliers
        serializer = SupplierSerializer(suppliers, many=True)
        # Return serialized data as a JSON response
        return Response(serializer.data)

    elif request.method == 'POST':
        # Deserialize request data into
        # a SupplierSerializer instance
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid serializer data to the database
            serializer.save()
            # Return serialized data of the newly
            # created supplier with 201 Created status
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        # Return errors if serializer data is
        # not valid with 400 Bad Request status
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def supplier_detail(request, pk):
    """
    Retrieve, update or delete a supplier.

    GET:
    Retrieve details of a specific supplier.

    PUT:
    Update details of a specific supplier based on request data.
    """
    try:
        # Attempt to retrieve the supplier with the given primary key
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        # Return 404 Not Found if supplier
        # with pk does not exist
        return Response(
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize and return the details of the retrieved supplier
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Deserialize request data into a SupplierSerializer
        # instance with current supplier instance
        serializer = SupplierSerializer(
            supplier, data=request.data)
        if serializer.is_valid():
            # Save the valid serializer data to update the supplier
            serializer.save()
            # Return serialized data of the updated supplier
            return Response(serializer.data)
        # Return errors if serializer data is not valid 
        # with 400 Bad Request status
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)
