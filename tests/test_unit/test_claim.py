from datetime import datetime
from coupons.claiming import claim_coupon


def test_get_non_claimed_coupon(storage, coupon):
    not_claimed = storage.get(coupon)
    not_claimed.claimed_at = datetime.now()
    second_not_claimed = storage.get(coupon)

    assert not second_not_claimed.claimed_at
    assert not_claimed is not second_not_claimed


def test_coupon_claim(coupon, storage):
    claimed = claim_coupon(coupon, storage=storage)

    assert claimed.claimed_at
    assert claimed is not coupon
