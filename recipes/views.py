from django.shortcuts import render
from models import Recipes
from rest_framework import generics

from recipes.serializers import RecipesSerializer


# Create your views here.
class RecipesView(generics.ListCreateAPIView):
    """
    API Create recipe and List recipes
    """

    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class RecipesView(generics.RetrieveUpdateDestroyAPIView):
    """
    API Update recipe and delete recipe
    """

    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
