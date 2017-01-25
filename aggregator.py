"""
Given a list of components and their individual nutritional value, build an aggregated store
"""

def aggregate_nuts(components):
    uniques = {}
    for component in components:
        for k,v in component.items():
            if uniques.get(k):
                uniques[k] = uniques[k] + v
            else:
                uniques[k] = v

    return uniques

def test_aggregate_nuts():
    data = [
        {
            'proteins'  : 100,
            'carbs'     : 200,
            'fats'      : 300
        },
        {
            'proteins': 99,
            'carbs': 299,
            'fats': 399
        }
    ]
    print aggregate_nuts(data) == {
        'fats' : 699, 'carbs' : 499, 'proteins' : 199
    }

test_aggregate_nuts()