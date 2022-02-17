from datetime import datetime


def test_get_first_non_claimed_coupon(storage, coupon):
    first_non_claimed = storage.get(coupon)
    first_non_claimed.claimed_at = datetime.now()

    second_non_claimed = storage.get(coupon)
    assert second_non_claimed is not first_non_claimed