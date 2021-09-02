from django.db import connection
from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
# Create your views here.

from .models import People
from .serializers import PeopleSerializer

class PeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows peoples to be viewed, edited and deleted.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # You can add additional logic here
        return super(PeopleViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).destroy(request, *args, **kwargs)