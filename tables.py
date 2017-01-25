INGREDIENTS_NV_MAP = {
    'RICE' : {
        'CARBS' : 100,
        'PROTEIN' : 100,
        'FAT' : 50
    }
}


POSSIBLE_INGREDIENTS = [ 'RICE', 'DAL', 'BESAN', 'RAJMA', 'BROWN BREAD',
                'FLOUR', 'TOMATO'
]

POSSIBLE_NV = ['PROTEIN', 'FAT', 'CARB', 'VITAMINS']



import random

NUT_TABLE = {}
for item in POSSIBLE_INGREDIENTS:
    components = random.sample(POSSIBLE_NV, random.randint(1, len(POSSIBLE_NV)))
    ret = {

    }
    for c in components:
        ret[c] = random.randint(10, 100)

    NUT_TABLE[item] = ret

print NUT_TABLE