from django.db import models
from rest_framework import serializers

from .models import People

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'url', 'first_name', 'last_name', 'email', 'profession']