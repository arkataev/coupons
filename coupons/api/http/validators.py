from django.conf import settings
from rest_framework.exceptions import ValidationError


def coupon_discount_validator(value):
    try:
        valid = 0.0 <= value <= 1.0
    except TypeError:
        pass
    else:
        if valid:
            return

    raise ValidationError(detail="Discount should be float 0.0 <= discount <= 1.0")


def coupon_amount_validator(value):
    try:
        valid = settings.MAX_COUPONS >= value >= 0
    except TypeError:
        pass
    else:
        if valid:
            return

    raise ValidationError(detail=f"Amount should be integer {settings.MAX_COUPONS} >= value >= 0")


def email_validator(value):
    if not value or type(value) is not str:
        raise ValidationError(detail='Email required')
