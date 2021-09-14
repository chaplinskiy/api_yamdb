import datetime as dt

from rest_framework.serializers import ValidationError


def year_validator(value):
    year = dt.date.today().year
    if value < 1 or value > year:
        raise ValidationError('Проверьте год!')
    return value
