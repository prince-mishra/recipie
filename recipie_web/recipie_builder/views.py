from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


def index(request):
    ctx = {
        'contents' : "hello"
    }
    return render_to_response('recipie_builder/index.html',ctx)


@csrf_exempt
def recipie_to_nut(request):
    txt = request.GET.get('text')
    ret = [
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

    return HttpResponse(json.dumps(ret))
