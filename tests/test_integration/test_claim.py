from datetime import datetime

from src.coupons.claiming import claim_coupon


def test_get_non_claimed_coupon(brand, storage):
    not_claimed = storage.get(brand)
    not_claimed.claimed_at = datetime.now()
    second_not_claimed = storage.get(brand)

    assert not hasattr(second_not_claimed, "claimed_at")
    assert not_claimed is not second_not_claimed


def test_coupon_claim(brand, storage):
    coupon = claim_coupon(brand=brand, storage=storage)

    assert coupon.claimed_at
