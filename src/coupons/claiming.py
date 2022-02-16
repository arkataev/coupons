from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .generate import Coupon, Brand

__all__ = ['User', 'AlreadyClaimed', 'claim_coupon']


@dataclass
class User:
    user_id: str
    coupon: Optional[Coupon] = None


class AlreadyClaimed(Exception):
    """Coupon was already claimed"""


def claim_coupon(user: User, brand: Brand) -> Coupon:
    """Returns a Coupon for a User if it's not already has one"""
    if user.coupon:
        raise AlreadyClaimed(f'User {user.user_id} already claimed a coupon')

    coupon = brand.get_non_claimed_coupon()
    coupon.claimed_at = datetime.now()

    return coupon
