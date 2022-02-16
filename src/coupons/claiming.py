from datetime import datetime
from typing import Optional

from .common import Coupon, Brand
from .storage import CouponStorage

__all__ = ['claim_coupon']


def claim_coupon(brand: Brand, storage: CouponStorage) -> Optional[Coupon]:
    """Claims coupon from storage for a given brand"""
    coupon = storage.get(brand)
    if coupon:
        coupon.claimed_at = datetime.now()

    return coupon
