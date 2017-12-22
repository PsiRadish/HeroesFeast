import json
from django.db import models as djangorm
import django.db.utils
from django.core.validators import MaxValueValidator, MinValueValidator

from hfapp.models import Hero, Skill

class DefaultSkill(djangorm.Model):
#{
    hero = djangorm.ForeignKey(Hero, on_delete=djangorm.PROTECT)
    skill = djangorm.ForeignKey(Skill, on_delete=djangorm.PROTECT)
    stars_required = djangorm.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class Meta:
        unique_together = ('hero', 'skill')
    
    def __str__(self):
        return '' % ()
    def __repr__(self):
        return 'WeaponType %s' % json.dumps(self, indent='  ')
#}
