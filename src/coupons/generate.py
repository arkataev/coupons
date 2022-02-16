import datetime
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Iterator
from typing import Optional

__all__ = ['create_coupons', 'Coupon', 'Brand']


@dataclass
class Coupon:
    discount: float
    code: Optional[str] = None
    created_at: Optional[datetime] = None
    claimed_at: Optional[datetime] = None
    used_at: Optional[datetime] = None


class Brand:
    brand_id: int

    def get_non_claimed_coupon(self) -> Coupon:
        """Return next non-claimed coupon"""


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
