from django.contrib.auth.models import  Group
from rest_framework import serializers

from demo.cbv_demo.models import User


class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = None


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']