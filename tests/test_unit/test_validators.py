import pytest
from django.conf import settings
from rest_framework.exceptions import ValidationError

from coupons.api.http import validators


@pytest.mark.parametrize('value', [None, 1])
def test_invalid_email(value):
    with pytest.raises(ValidationError):
        validators.email_validator(value)


@pytest.mark.parametrize('value', [None, settings.MAX_COUPONS + 1, -1])
def test_invalid_coupon_amount(value):
    with pytest.raises(ValidationError):
        validators.coupon_amount_validator(value)


@pytest.mark.parametrize('value', [None, -1, 1.1])
def test_invalid_coupon_discount(value):
    with pytest.raises(ValidationError):
        validators.coupon_discount_validator(value)
