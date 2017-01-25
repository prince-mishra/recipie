"""
Given a list of components and their individual nutritional value, build an aggregated store
"""
from sys import path
path.append('/Users/mishraprince/work/scripts/healthifyme/recipie')

from NUTRITION_VALUE_TABLE import INGREDIENTS

def aggregate_nuts(components):
    uniques = {}
    missed = []

    for component in components:
        k = component['name']
        v = component['quantity']

        if v==0:
            missed.append(k)

        nutritional_items = INGREDIENTS.get(k, {})
        for name,value in nutritional_items.items():
            cur_value = value*v/100.0
            if uniques.get(name):
                uniques[name] = uniques[name] + cur_value
            else:
                uniques[name] = cur_value
    return (uniques, missed)


#test_aggregate_nuts()