from django.db import models as djangorm
import django.db.utils
from util import staticproperty

# declare identifiers for Color constants
RED       = None
GREEN     = None
BLUE      = None
COLORLESS = None

class Color(djangorm.Model):
#{
    id   = djangorm.CharField(max_length=2, primary_key=True)
    name = djangorm.CharField(max_length=10)
    
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

# give constants their values now that Color is defined
try:
    RED       = Color.objects.filter(pk='1R').first() #, name='red')
    GREEN     = Color.objects.filter(pk='2G').first() #, name='green')
    BLUE      = Color.objects.filter(pk='3B').first() #, name='blue')
    COLORLESS = Color.objects.filter(pk='4_').first() #, name='colorless')
except django.db.utils.OperationalError:
    pass
