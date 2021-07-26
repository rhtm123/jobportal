from django.urls import path
from job import views

urlpatterns = [
    # path("locations", views.locations,),

    path('locations/', views.LocationListCreate.as_view()),
    path('location/<int:pk>/', views.LocationGetUpdate.as_view()),
    path('location/delete/<int:pk>/', views.LocationDelete.as_view()),
]