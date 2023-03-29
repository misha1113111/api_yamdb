import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Неправильное имя пользователя!'
        )
    if not bool(re.match(r'^[\w.@+-]+$', value)):
        raise ValidationError(
            'Неправильные символы в username'
        )
    return value