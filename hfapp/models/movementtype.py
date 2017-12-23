from django.db import models as djangorm
import django.db.utils
from util import staticproperty

# declare identifiers for MovementType constants
INFANTRY = None
CAVALRY  = None
ARMORED  = None
FLIER    = None

class MovementType(djangorm.Model):
#{
    id   = djangorm.CharField(max_length=4, primary_key=True)
    name = djangorm.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return 'MovementType {name: "%s"}' % self.name
    
    @staticproperty
    def INFANTRY():
        return INFANTRY
    
    @staticproperty
    def CAVALRY():
        return CAVALRY
    
    @staticproperty
    def ARMORED():
        return ARMORED
    
    @staticproperty
    def FLIER():
        return FLIER
#}

# give constants their values now that MovementType is defined
try:
    INFANTRY = MovementType.objects.filter(pk='1Inf').first()
    CAVALRY  = MovementType.objects.filter(pk='2Cav').first()
    ARMORED  = MovementType.objects.filter(pk='3Arm').first()
    FLIER    = MovementType.objects.filter(pk='4Fly').first()
except django.db.utils.OperationalError:
    pass
