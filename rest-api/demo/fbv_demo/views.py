from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demo.cbv_demo.models import Venue
from rest_framework import status


@api_view(['POST'])
def save_venue(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    geo_location = request.POST.get('geo_location')
    try:
        Venue.objects.create(name=name, address=address, geo_location=geo_location)
        return Response("Data Saved!", status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(ex, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_venue(request):
    return Response(Venue.objects.all().values(), status=status.HTTP_200_OK)
