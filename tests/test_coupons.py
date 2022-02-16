import uuid
from unittest import mock

import pytest

from src.coupons.claiming import User, claim_coupon, AlreadyClaimed
from src.coupons.generate import create_coupons, Coupon, Brand


@pytest.fixture
def coupon():
    return Coupon(discount=0.2)


@pytest.fixture
def brand_mock():
    return mock.create_autospec(Brand, instance=True)


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


def test_coupon_claim(brand_mock, coupon):
    brand_mock.get_non_claimed_coupon.return_value = coupon
    coupon = claim_coupon(User(user_id=str(uuid.uuid4())), brand=brand_mock)
    assert coupon.claimed_at


def test_coupon_claimed(coupon, brand_mock):
    user = User(user_id=str(uuid.uuid4()), coupon=coupon)
    with pytest.raises(AlreadyClaimed):
        claim_coupon(user, brand=brand_mock)
