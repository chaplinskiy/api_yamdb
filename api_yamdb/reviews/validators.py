from django.utils import timezone

from rest_framework.serializers import ValidationError


def year_validator(value):
    if value < 1 or value > timezone.now().year:
        raise ValidationError('Проверьте год!')
    return value


def let_me_name_you_as_i_want():
    pass
