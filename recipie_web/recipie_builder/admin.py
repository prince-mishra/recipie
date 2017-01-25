from django.contrib import admin

from recipie_builder.models import Food, Ingredient
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'nutritional_value']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'food']


admin.site.register(Food, FoodAdmin)
admin.site.register(Ingredient, IngredientAdmin)
