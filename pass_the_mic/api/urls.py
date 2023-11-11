# This file returns the main function if the route handler is empty

from django.urls import path
#This line imports the main function from the views.py in the api directory
from .views import main

urlpatterns = [
    path('', main),
    path('home', main),
]
