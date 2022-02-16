import heapq
from abc import abstractmethod
from collections import defaultdict
from typing import List, Dict

from .common import Coupon, Brand


class CouponStorage:
    @abstractmethod
    def add(self, coupon: Coupon) -> None:
        raise NotImplemented

    @abstractmethod
    def get(self, brand: Brand) -> Coupon:
        raise NotImplemented


class CouponHeapStorage(CouponStorage):
    """Return non-claimed coupon in O(1)"""

    def __init__(self):
        self._brands: Dict[str: List[Coupon]] = defaultdict(list)

    def add(self, coupon: Coupon):
        heapq.heappush(self._brands[coupon.brand.brand_id], coupon)

    def get(self, brand: Brand) -> Coupon:
        pq = self._brands[brand.brand_id]
        while pq:
            coupon = pq[0]
            if coupon.claimed_at:
                heapq.heappop(pq)
            else:
                return coupon
