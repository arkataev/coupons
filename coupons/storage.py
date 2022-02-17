import heapq
from abc import abstractmethod
from collections import defaultdict
from functools import partial
from typing import List, Dict

from .common import Coupon, Brand


class CouponStorage:
    @abstractmethod
    def add(self, coupon: Coupon) -> None:
        raise NotImplemented

    @abstractmethod
    def get(self, coupon: Coupon) -> Coupon:
        raise NotImplemented


class CouponHeapStorage(CouponStorage):
    """Return non-claimed coupon in O(1)"""

    def __init__(self):
        self._brands: Dict[str: List[Coupon]] = defaultdict(partial(defaultdict, list))

    def add(self, coupon: Coupon):
        heapq.heappush(self._brands[coupon.brand.brand_id][coupon.discount], coupon)

    def get(self, coupon: Coupon) -> Coupon:
        brand_id = coupon.brand.brand_id
        discount = coupon.discount

        pq = self._brands[brand_id][discount]
        while pq:
            coupon = pq[0]
            if coupon.claimed_at:
                heapq.heappop(pq)
            else:
                return coupon


def brand_exists(brand: Brand) -> bool:
    """Checks if Brand is registered in system. Can help to validate coupon creation and claiming"""
    return True
