from django.db import models as djangorm
import django.db.utils
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from util import staticproperty

from hfapp.models import WeaponType

# declare identifiers for SkillType constants
SKILLTYPE_WEAPON  = None
SKILLTYPE_SUPPORT = None
SKILLTYPE_SPECIAL = None
SKILLTYPE_A       = None
SKILLTYPE_B       = None
SKILLTYPE_C       = None
SKILLTYPE_S       = None

class SkillType(djangorm.Model):
#{
    id   = djangorm.CharField(max_length=3, primary_key=True)
    name = djangorm.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return 'SkillType {name: "%s"}' % self.name
    
    @staticproperty
    def WEAPON():
        return SKILLTYPE_WEAPON
    @staticproperty
    def SUPPORT():
        return SKILLTYPE_SUPPORT
    @staticproperty
    def SPECIAL():
        return SKILLTYPE_SPECIAL
    @staticproperty
    def A():
        return SKILLTYPE_A
    @staticproperty
    def B():
        return SKILLTYPE_B
    @staticproperty
    def C():
        return SKILLTYPE_C
    @staticproperty
    def S():
        return SKILLTYPE_S
#}
# give constants their values now that SkillType is defined
try:
    SKILLTYPE_WEAPON  = SkillType.objects.filter(pk='1Wp')
    SKILLTYPE_SUPPORT = SkillType.objects.filter(pk='2Su')
    SKILLTYPE_SPECIAL = SkillType.objects.filter(pk='3Sp')
    SKILLTYPE_A       = SkillType.objects.filter(pk='4A')
    SKILLTYPE_B       = SkillType.objects.filter(pk='5B')
    SKILLTYPE_C       = SkillType.objects.filter(pk='6C')
    SKILLTYPE_S       = SkillType.objects.filter(pk='7S')
except django.db.utils.OperationalError:
    pass


class Skill(djangorm.Model):
#{
    name = djangorm.CharField(max_length=40)
    skill_type   = djangorm.ForeignKey(SkillType,  on_delete=djangorm.PROTECT, related_name='skills_of_type')
    weapon_type  = djangorm.ForeignKey(WeaponType, on_delete=djangorm.PROTECT, related_name='weapons_of_type',  null=True, default=None)
    description  = djangorm.TextField()
    inheritable  = djangorm.BooleanField(default=True)
    prerequisite = djangorm.ForeignKey('self',     on_delete=djangorm.PROTECT, related_name='prerequisite_for', null=True, default=None)
    
    __no_weapon_type_message = _("Weapon skills need a Weapon Type.")
    def clean(self):
        # If skill_type is SkillType.WEAPON, weapon_type cannot be None
        if self.skill_type == SkillType.WEAPON and self.weapon_type == None:
            raise ValidationError(self.__no_weapon_type_message, code='weapon_type_missing')
#}
