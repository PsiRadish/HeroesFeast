from django.db import models as modjels
from hfapp.constants import WEAPON_GROUP
from util import staticproperty

GROUP_SWORD  = None
GROUP_LANCE  = None
GROUP_AXE    = None
GROUP_BOW    = None
GROUP_DAGGER = None
GROUP_TOME   = None
GROUP_STAFF  = None
GROUP_BREATH = None

class WeaponGroup(modjels.Model):
    