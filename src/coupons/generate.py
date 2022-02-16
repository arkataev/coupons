import uuid
from datetime import datetime
from typing import Iterator

from .common import Coupon


__all__ = ['create_coupons']


def create_coupons(coupon: Coupon, amount: int = 1) -> Iterator[Coupon]:
    """Generates a given amount of coupons"""
    if amount < 0:
        raise ValueError('Generatated coupons amount should be >= 0')

    for _ in range(amount):
        coupon.created_at = datetime.now()
        coupon.code = _make_coupon_code()
        yield coupon


def _make_coupon_code() -> str:
    return str(uuid.uuid4())
