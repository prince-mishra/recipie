#!/usr/bin/python
#  -*- coding: utf-8 -*-
from unittest import TestCase

import recipe_parsers
from nutrition_chart_builder import build


class TestRecipie(TestCase):
    def setUp(self):
        self.recipes = [
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
    def test_x(self):
        results = {'protien': 10, 'carbs': 25, 'energy': 120}
        self.assertEqual(build(self.recipes[0]), results)

    def test_simple_parser(self):
        parser = recipe_parsers.SimpleRecipeParser()
        parser.parse(self.recipes[0])
