import pytest

from coupons.common import Coupon
from coupons.generate import create_coupons


def test_create_coupons(coupon):
    created = create_coupons(coupon)

    for c in created:
        assert c.code
        assert c.created_at
        assert not c.claimed_at
        assert not c.used_at


def test_create_coupons_invalid_amount(coupon):
    with pytest.raises(ValueError):
        list(create_coupons(coupon, amount=-1))


def test_coupons_lt(brand):
    c1 = Coupon(brand, 0.2)
    c2 = Coupon(brand, 0.2)

    assert c1 == c2
    c1.claimed_at = True
    assert c1 > c2
