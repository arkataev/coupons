import datetime
import uuid
from typing import Iterator

from .._dataclasses import Coupon

__all__ = ['create_coupons']


def _make_coupon_code() -> str:
    """Generates a unique alpha-numeric code"""
    return str(uuid.uuid4())


def create_coupons(coupon: Coupon, amount: int = 1) -> Iterator[Coupon]:
    if amount < 0:
        raise ValueError('Generatated coupons amount should be >= 0')

    for _ in range(amount):
        coupon.created_at = datetime.datetime.now()
        coupon.coupon_code = _make_coupon_code()
        yield coupon
