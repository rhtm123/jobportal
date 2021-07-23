from django.urls import path
from account import views

urlpatterns = [
	path('login/',views.mylogin),
	path('register/',views.register),
	path('logout/',views.mylogout),
]