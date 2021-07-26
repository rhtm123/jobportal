

from .models import Job, Location, JobLocation

from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'