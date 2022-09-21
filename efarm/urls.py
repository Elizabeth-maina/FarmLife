from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('farmers_list/', FarmersList, name='farmers'),
    path("add_farmer/", addFarmer, name='add_farmer'),

]