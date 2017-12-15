from django.db import models as modjels
from hfapp.constants import COLOR
from util import staticproperty

RED       = None
GREEN     = None
BLUE      = None
COLORLESS = None

class Color(modjels.Model):
#{
    name = modjels.CharField(max_length=10, primary_key=True)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return 'Color {name: "%s"}' % self.name
    
    @staticproperty
    def RED():
        return RED
    @staticproperty
    def GREEN():
        return GREEN
    @staticproperty
    def BLUE():
        return BLUE
    @staticproperty
    def COLORLESS():
        return COLORLESS
#}

# I am a genius!
RED       = Color(name=COLOR.RED)
GREEN     = Color(name=COLOR.GREEN)
BLUE      = Color(name=COLOR.BLUE)
COLORLESS = Color(name=COLOR.COLORLESS)
