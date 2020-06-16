from MySQLdb._mysql import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from demo.cbv_demo.models import Venue
from demo.cbv_demo.serializers import VenueSerializer


@api_view(['GET', 'POST'])
def get_venues(request):
    try:
        if request.method == 'GET':
            venues = Venue.objects.all()
            venue_serializer = VenueSerializer(venues, many=True)
            return JsonResponse(venue_serializer.data, safe=False)
        elif request.method == 'POST':
            venue_data = JSONParser().parse(request)
            venue_serializer = VenueSerializer(data=venue_data)
            if venue_serializer.is_valid():
                venue_serializer.save()
                print(venue_serializer)
                return JsonResponse(venue_serializer.data, status=status.HTTP_201_CREATED)
    except Exception as exception:
        return Response({
            "message": str(exception)
        }, status=500)


@api_view(['PUT', 'GET', 'DELETE'])
def venue(request, pk):
    try:
        venue = Venue.objects.get(pk=pk)
    except Venue.DoesNotExist:
        return JsonResponse({'message': 'The venue does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        venue_serializer = VenueSerializer(venue)
        return JsonResponse(venue_serializer.data)

    elif request.method == 'PUT':
        venue_data = JSONParser().parse(request)
        venue_serializer = VenueSerializer(venue, data=venue_data)
        if venue_serializer.is_valid():
            venue_serializer.save()
            return JsonResponse(venue_serializer.data)
        return JsonResponse(venue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue.delete()
        return JsonResponse({'message': 'Venue was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
