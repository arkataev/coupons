from dataclasses import dataclass
from datetime import datetime
from typing import Optional

__all__ = ['Coupon', 'User', 'Brand']


@dataclass
class Brand:
    brand_id: int


@dataclass
class Coupon:
    brand: Brand
    discount: float
    coupon_code: Optional[str] = None
    created_at: Optional[datetime] = None
    claimed_at: Optional[datetime] = None
    used_at: Optional[datetime] = None


@dataclass
class User:
    user_id: str
    coupon: Coupon
