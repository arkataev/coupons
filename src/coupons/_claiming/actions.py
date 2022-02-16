from .._dataclasses import User, Coupon


def claim_coupon(user: User) -> Coupon:
    """Returns a coupon code for a User if it's not already has one"""

