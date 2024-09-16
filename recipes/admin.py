from django.contrib import admin

from .models import Ingredients, Recipes

admin.site.register(Recipes)
admin.site.register(Ingredients)
