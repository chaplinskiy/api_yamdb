import datetime as dt

from rest_framework.serializers import ValidationError


def year_validator(value):
    year = dt.date.today().year
    # if not (year - 40 < value <= year):
    if value < 1 or value > year:
        raise ValidationError('Проверьте год!')
    return value
