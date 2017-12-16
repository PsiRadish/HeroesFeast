
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class InListValidator:
#{
    valid_list = []
    
    message = _('Value %(value)s is not in the list of accepted values: %(valid_list)s')
    code = 'value_not_in_accepted_list'

    def __init__(self, valid_list, message=None, code=None):
        self.valid_list = valid_list
        if message:
            self.message = message
        if code:
            self.code = code

    def __call__(self, value):
        if not value in self.valid_list:
            raise ValidationError(
                self.message,
                code = self.code,
                params = dict(value=value, valid_list=self.valid_list)
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.valid_list == other.valid_list and
            self.message == other.message and
            self.code == other.code
        )
#}
