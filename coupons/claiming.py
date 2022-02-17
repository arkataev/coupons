from datetime import datetime
from typing import Optional

from .common import Coupon, User
from .storage import CouponStorage


__all__ = ['claim_coupon', 'already_claimed']


def claim_coupon(coupon: Coupon, storage: CouponStorage) -> Optional[Coupon]:
    """Claims coupon from storage for a given brand"""
    _coupon = storage.get(coupon)

    if _coupon:
        _coupon.claimed_at = datetime.now()

    return _coupon


def already_claimed(user: User) -> bool:
    """Check if User already claimed a coupon"""
    return True if user.coupon else False
