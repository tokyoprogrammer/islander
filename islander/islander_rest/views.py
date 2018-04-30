from django.shortcuts import render

from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from islander_rest.models import *
from islander_rest.serializers import *

# Create your views here.

class FoodCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categorys to be viewed or added.
    """
    queryset = FoodCategory.objects.all().order_by('id')
    serializer_class = FoodCategorySerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restaurants to be viewed or added.
    """
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer

