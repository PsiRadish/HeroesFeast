from django.db import models as djangorm
from django.db.models import Q
import django.db.utils

from hfapp.models import Color, WeaponGroup, WeaponType, MovementType
from hfapp.models import Hero
from hfapp.models.validators import InListValidator

# validate_op = InListValidator(['and', 'or'])
validate_range = InListValidator([1, 2], code="validate_range")

class SkillRequirement(djangorm.Model):
    is_head       = djangorm.BooleanField()
    next          = djangorm.OneToOneField('self', djangorm.CASCADE, related_name='previous', null=True, default=None)
    # next_op     = djangorm.CharField(max_length=3, validators=[validate_op])

    description   = djangorm.TextField()
    negate        = djangorm.BooleanField(default=False)
    range         = djangorm.PositiveSmallIntegerField(validators=[validate_range], null=True, default=False)
    weapon_group  = djangorm.ForeignKey(WeaponGroup,  null=True, default=False)
    color         = djangorm.ForeignKey(Color,        null=True, default=False)
    movement_type = djangorm.ForeignKey(MovementType, null=True, default=False)

    def to_q(self, queryset):
        q = Q()

        if self.range:
            q = q & Q(weapon_type__range__exact = self.range)
        if self.weapon_group:
            q = q & Q(weapon_type__weapon_group__exact = self.weapon_group)
        if self.color:
            q = q & Q(weapon_type__color__exact = self.color)
        if self.movement_type:
            q = q & Q(movement_type__exact = self.movement_type)

        if self.negate:
            q = ~q;

        if self.next:
            return q & self.next.to_q()
        else:
            return q