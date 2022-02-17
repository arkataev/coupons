from dataclasses import dataclass
from datetime import datetime
from typing import Optional

__all__ = ['Brand', 'Coupon', 'User']


@dataclass
class Brand:
    brand_id: str


@dataclass
class Coupon:
    brand: Brand
    discount: float
    code: Optional[str] = None
    created_at: Optional[datetime] = None
    claimed_at: Optional[datetime] = None
    used_at: Optional[datetime] = None

    def __str__(self):
        return f"{self.code}:{self.discount * 100}%"

    def __lt__(self, other: "Coupon"):
        return False if self.claimed_at else True


@dataclass
class User:
    user_id: str
    coupon: Optional[Coupon] = None
