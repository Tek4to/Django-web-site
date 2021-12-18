from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Parking
from .serializers import ParkingSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def parking_list(request):
    if request.method == 'GET':
        parkings = Parking.objects.all()
        parkings_serializer = ParkingSerializer(parkings, many=True)
        return JsonResponse(parkings_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        parking_data = JSONParser().parse(request)
        parking_serializer = ParkingSerializer(data=parking_data)
        if parking_serializer.is_valid():
            parking_serializer.save()
            return JsonResponse(parking_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(parking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Parking.objects.all().delete()
        return JsonResponse({'message': '{} Parkings were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def parking_detail(request, pk):
    try:
        parking = Parking.objects.get(pk=pk)
    except Parking.DoesNotExist:
        return JsonResponse({'message': 'The parking does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        parking_serializer = ParkingSerializer(parking)
        return JsonResponse(parking_serializer.data)

    elif request.method == 'PUT':
        parking_data = JSONParser().parse(request)
        parking_serializer = ParkingSerializer(parking, data=parking_data)
        if parking_serializer.is_valid():
            parking_serializer.save()
            return JsonResponse(parking_serializer.data)
        return JsonResponse(parking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        parking.delete()
        return JsonResponse({'message': 'Parking was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
