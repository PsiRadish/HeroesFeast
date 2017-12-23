import json
from django.db import models as djangorm
import django.db.utils

from hfapp.models import WeaponType, MovementType

class Hero(djangorm.Model):
#{
    name = djangorm.CharField(max_length=50)
    weapon_type = djangorm.ForeignKey(WeaponType, on_delete=djangorm.DO_NOTHING, related_name='heroes_using_weapon_type')
    movement_type = djangorm.ForeignKey(MovementType, on_delete=djangorm.DO_NOTHING, related_name='heroes_with_movement_type')
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return 'WeaponType %s' % json.dumps(self, indent='  ')
#}
