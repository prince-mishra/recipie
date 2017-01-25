from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from recipie_builder.models import Food, Ingredient


class FoodResource(ModelResource):
    nutritionals = fields.DictField(attribute='nutritional_value')

    class Meta:
        queryset = Food.objects.all()
        resource_name = 'food'
        authorization = Authorization()
        authentication = Authentication()
        always_return_data = True


class IngredientResource(ModelResource):
    food = fields.ForeignKey(FoodResource, 'food')

    class Meta:
        queryset = Ingredient.objects.all()
        resource_name = 'ingredient'
        authorization = Authorization()
        authentication = Authentication()
        always_return_data = True
