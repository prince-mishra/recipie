import csv
import sys
import os
import pprint

if __name__=="__main__":
    filepath = os.path.abspath(sys.argv[1])
    data_set = {}
    with open(filepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            name, protein, fats, carbs, fiber = row
            data_set[name.lower()] = {
                'protein' : protein,
                'fats' : fats,
                'carbs' : carbs,
                'fiber' : fiber
            }
    pprint.pprint(data_set)

