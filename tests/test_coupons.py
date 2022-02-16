from src.coupons import create_coupons, Coupon, Brand
import pytest


def test_create_coupons():
    coupon = Coupon(Brand(1), discount=0.2)
    created = create_coupons(coupon)

    for c in created:
        assert c.coupon_code
        assert c.created_at
        assert not c.claimed_at
        assert not c.used_at


def test_create_coupons_invalid_amount():
    coupon = Coupon(Brand(1), discount=0.2)

    with pytest.raises(ValueError):
        list(create_coupons(coupon, amount=-1))

