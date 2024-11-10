from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


# def validate_username(value):
#     if not value.isalnum() and '_' not in value:
#         raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
# isalnum won't work because of the underscore inclusion
# we use value.lower() because slugify automatically lowers

@deconstructible
class UsernameValidator:
    def __init__(self, message=None):
        self.message = message
    
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Ensure this value contains only letters, numbers, and underscore.'
        else:
            self.__message = value
    
    def __call__(self, value, *args, **kwargs):
        if '-' in value or value.lower() != slugify(value):
            raise ValidationError(self.message)
