from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from . import views

from tastypie.api import Api
from recipie_builder.api import FoodResource, IngredientResource

v1_api = Api(api_name='v1')
v1_api.register(FoodResource())
v1_api.register(IngredientResource())

urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
    url(
        regex=r'^recipie_to_nut$',
        view=views.recipie_to_nut,
        name='recipie_to_nut'
    ),
    url(r'^api/', include(v1_api.urls)),

]
