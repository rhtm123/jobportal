from django.shortcuts import render, HttpResponse
# Create your views here.
from django.core import serializers


from .models import Location
from .serializers import LocationSerializer, JobLocation, JobLocationSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

def locations(request):
    all_locations = Location.objects.all()
    json_list = serializers.serialize('json', all_locations)
    return HttpResponse(json_list)

class CustomPagination(PageNumberPagination):
	page_size = 15


class LocationListCreate(generics.ListCreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	# filter_backends = (DjangoFilterBackend,)
	# filter_fields = ('is_published',)
	pagination_class = CustomPagination


class LocationGetUpdate(generics.RetrieveUpdateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = (AllowAny,)

class LocationDelete(generics.DestroyAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)