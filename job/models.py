from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city


class Job(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobLocation(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE) 