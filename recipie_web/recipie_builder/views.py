#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from sys import path
path.append('/Users/mishraprince/work/scripts/healthifyme/recipie')

from recipe_parsers import SimpleRecipeParser
from aggregator import aggregate_nuts

parser = SimpleRecipeParser()

# Create your views here.


def index(request):
    ctx = {
        'contents' : "hello"
    }
    return render_to_response('recipie_builder/index.html',ctx)


@csrf_exempt
def recipie_to_nut(request):
    txt = request.POST.get('text')
    print "RECIPIE TO NUT ", txt
    parsed = parser.parse(txt.encode('utf-8'))
    print "PARSED ", parsed
    processed, missed, sum_quantity = aggregate_nuts(parsed['ingredients'])
    # TODO
    processed_per_100 = {}
    for k,v in processed.items():
        processed_per_100[k] =(v/sum_quantity)*100


    return HttpResponse(json.dumps({"nutritional_values" : processed_per_100, "missed_ingredients" : ",".join(missed), "ingredients" : parsed}))
