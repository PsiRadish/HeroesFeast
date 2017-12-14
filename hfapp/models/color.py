from django.db import models
from util import staticproperty

RED       = None
GREEN     = None
BLUE      = None
COLORLESS = None

class Color(models.Model):
#{
    name = models.CharField(max_length=10, primary_key=True)
    
    def __str__(self):
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

RED       = Color(name = "red")
GREEN     = Color(name = "green")
BLUE      = Color(name = "blue")
COLORLESS = Color(name = "colorless")