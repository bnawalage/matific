from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets

from demo.cbv_demo.serializers import GeneralSerializer
from django.apps import apps


class GeneralViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        model = apps.get_model("cbv_demo", self.kwargs.get('model'))
        return model.objects.all()

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.kwargs.get('model')
        return GeneralSerializer


