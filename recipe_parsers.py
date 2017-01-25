#!/usr/bin/python
#  -*- coding: utf-8 -*-
from MEASUREMENT_NAME_TABLE import NAME_MAP


class BaseRecipeParser:
    def __init__(self):
        pass

    def parse(self, recipe_text):
        pass


class SimpleRecipeParser(BaseRecipeParser):
    def parse(self, recipe_text):
        ingredients_info = []
        ingredients_str = recipe_text.split('\n')
        for ingredient in ingredients_str:
            ingredient_data = self._get_ingredient_data(ingredient)
            if ingredient_data:
                ingredients_info.append(ingredient_data)
        return {'ingredients': ingredients_info, 'measurement': 'gram'}

    def _get_ingredient_data(self, ingredient_str):
        tokens = [token.strip() for token in ingredient_str.split('-')]
        if len(tokens) < 2:
            return
        ingredient_name = self.get_ingredient_name('-'.join(tokens[:-1]))
        quantity = self.get_absolute_quantity(tokens[-1])
        return {'name': ingredient_name, 'quantity': quantity}

    def get_ingredient_name(self, ingredient_name_str):
        # TODO: We need to improve this by dropping meaningless characters.
        return ingredient_name_str

    def get_absolute_quantity(self, quantity_str):
        tokens = [token.strip() for token in quantity_str.split(' ')]
        quantity = 0
        measure = None
        for token in tokens:
            try:
                quantity = float(token)
                break
            except ValueError:
                continue
        possible_measures = NAME_MAP.keys()
        for possible_measure in possible_measures:
            if possible_measure in tokens:
                measure = possible_measure
                break
        if quantity and measure:
            return quantity * NAME_MAP[measure]['value']
        return 0


recipes = [
    """Red Kidney beans (Rajma) - 1 cup
Onion - 1(finely minced)
Tomato - 2 (crushed or pureed)
Ginger-garlic paste - 1 tsp
Green chili - 1
Turmeric - ¼ tsp
Chilly powder - ½ tsp
Coriander /dhania powder - 1 tsp
Channa masala/ Garam Masala - ¼ tsp
Salt - to taste
Ghee - ¼ tsp
Oil - 1 tsp
Cumin seeds - ¼ tsp
Coriander leaves - for garnishing"""
]
parser = SimpleRecipeParser()
print parser.parse(recipes[0])
