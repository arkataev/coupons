from uuid import uuid4

import django
import pytest
from rest_framework.test import APIClient

from coupons.common import Brand, Coupon
from coupons.generate import create_coupons
from coupons.storage import CouponHeapStorage


@pytest.fixture
def brand():
    return Brand(brand_id=str(uuid4()))


@pytest.fixture
def coupon(brand):
    return Coupon(brand=brand, discount=0.2)


@pytest.fixture(scope='session')
def storage():
    return CouponHeapStorage()


@pytest.fixture(autouse=True)
def generate_coupons(storage, coupon):
    coupons = create_coupons(coupon, 10)
    for c in coupons:
        storage.add(c)


@pytest.fixture(scope='session')
def client():
    django.setup()
    return APIClient()
