"""
Given a list of components and their individual nutritional value, build an aggregated store
"""
from sys import path
path.append('/Users/mishraprince/work/scripts/healthifyme/recipie')

from NUTRITION_VALUE_TABLE import INGREDIENTS

def aggregate_nuts(components):
    uniques = {}
    missed = []
    sum_quantity = 0
    for component in components:
        k = component['name'].lower()
        v = component['quantity']
        sum_quantity += v
        nutritional_items = INGREDIENTS.get(k, {})

        if not (v and nutritional_items):
            missed.append(k)

        for name, value in nutritional_items.items():
            cur_value = float(value)*v/100.0
            if uniques.get(name):
                uniques[name] = uniques[name] + cur_value
            else:
                uniques[name] = cur_value
    return (uniques, missed, sum_quantity)


#test_aggregate_nuts()