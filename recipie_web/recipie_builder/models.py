from __future__ import unicode_literals

from django.db import models
import jsonfield
#jsonfield.JSONField()
# Create your models here.


class Food(models.Model):
    name = models.CharField(unique = True, max_length = 255)
    nutritional_value = jsonfield.JSONField()

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    food = models.ForeignKey(Food)
    name = models.CharField(max_length = 255)
    quantity = models.FloatField()
    unit = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name
