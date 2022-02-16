from uuid import uuid4

import pytest

from src.coupons.common import Brand, Coupon
from src.coupons.generate import create_coupons
from src.coupons.storage import CouponHeapStorage
from src.coupons.api.http.app import app


@pytest.fixture(scope='session')
def storage():
    return CouponHeapStorage()


@pytest.fixture
def brand():
    return Brand(brand_id=str(uuid4()))


@pytest.fixture
def coupon(brand):
    return Coupon(brand=brand, discount=0.2)


@pytest.fixture(autouse=True)
def generate_coupons(storage, coupon):
    coupons = create_coupons(coupon, 10)
    for c in coupons:
        storage.add(c)


@pytest.fixture(scope='session')
def client():
    app.config.update({"TESTING": True})
    yield app.test_client()
    app.config.update({"TESTING": False})
