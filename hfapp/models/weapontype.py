import json
from django.db import models as djangorm
import django.db.utils

from util import staticproperty
from hfapp.models.color import Color
from hfapp.models.validators import InListValidator
from hfapp.constants import STATS

# declare identifiers for WeaponGroup constants
GROUP_SWORD  = None
GROUP_LANCE  = None
GROUP_AXE    = None
GROUP_BOW    = None
GROUP_DAGGER = None
GROUP_TOME   = None
GROUP_STAFF  = None
GROUP_BREATH = None

class WeaponGroup(djangorm.Model):
#{
    id   = djangorm.CharField(max_length=2, primary_key=True)
    name = djangorm.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return 'WeaponGroup {name: "%s"}' % self.name
        
    @staticproperty
    def SWORD():
        return GROUP_SWORD
    @staticproperty
    def LANCE():
        return GROUP_LANCE
    @staticproperty
    def AXE():
        return GROUP_AXE
    @staticproperty
    def BOW():
        return GROUP_BOW
    @staticproperty
    def DAGGER():
        return GROUP_DAGGER
    @staticproperty
    def TOME():
        return GROUP_TOME
    @staticproperty
    def STAFF():
        return GROUP_STAFF
    @staticproperty
    def BREATH():
        return GROUP_BREATH
#}
# give constants their values now that WeaponGroup is defined
try:
    GROUP_SWORD  = WeaponGroup.objects.filter(pk='Sw').first()
    GROUP_LANCE  = WeaponGroup.objects.filter(pk='La').first()
    GROUP_AXE    = WeaponGroup.objects.filter(pk='Ax').first()
    GROUP_BOW    = WeaponGroup.objects.filter(pk='Bw').first()
    GROUP_DAGGER = WeaponGroup.objects.filter(pk='Dg').first()
    GROUP_TOME   = WeaponGroup.objects.filter(pk='Tm').first()
    GROUP_STAFF  = WeaponGroup.objects.filter(pk='St').first()
    GROUP_BREATH = WeaponGroup.objects.filter(pk='Br').first()
except django.db.utils.OperationalError:
    pass

validate_range = InListValidator([1, 2], code="validate_range")
validate_stat = InListValidator(STATS, code="validate_stat")

class WeaponType(djangorm.Model):
#{
    id      = djangorm.CharField(max_length=2, primary_key=True)
    name    = djangorm.CharField(max_length=20)
    group   = djangorm.ForeignKey(WeaponGroup, on_delete=djangorm.PROTECT, related_name='+')
    color   = djangorm.ForeignKey(Color,       on_delete=djangorm.PROTECT, related_name='weapon_types_of_color')
    range   = djangorm.PositiveSmallIntegerField(validators=[validate_range])
    vs_stat = djangorm.CharField(max_length=3, validators=[validate_stat])
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return 'WeaponType %s' % json.dumps(self, indent='  ')
#}
