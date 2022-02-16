from datetime import datetime


def test_get_first_non_claimed_coupon(storage, brand):
    first_non_claimed = storage.get(brand)
    first_non_claimed.claimed_at = datetime.now()

    second_non_claimed = storage.get(brand)
    assert second_non_claimed is not first_non_claimed