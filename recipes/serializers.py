from rest_framework import serializers

from .models import Recipes


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('title', 'ingredients', 'preparation_method')
