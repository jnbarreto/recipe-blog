from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.name


class Recipes(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredients, related_name='recipes')
    preparation_method = models.TextField(max_length=255)

    def __str__(self):
        return self.title
