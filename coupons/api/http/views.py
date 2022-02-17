from django.conf import settings
from django.http import JsonResponse, HttpResponse
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from coupons.claiming import claim_coupon, already_claimed
from coupons.common import Brand, User, Coupon
from coupons.generate import create_coupons
from coupons.storage import CouponHeapStorage, brand_exists
from . import validators
from .errors import AlreadyClaimed

# TODO: THIS IS FOR DEMO SINGLE-THREAD SERVER DEVELOPMENT ONLY
STORAGE = CouponHeapStorage()


class CouponView(APIView):
    def post(self, request):
        _data = request.data
        brand_id = _data.get('brand_id')
        data = _data.get('data', {})
        discount = data.get('discount', -1.0)
        amount = data.get('amount', -1)

        if not brand_exists(Brand(brand_id)):
            raise NotFound(f"Brand {brand_id} does not exist")

        validators.coupon_discount_validator(discount)
        validators.coupon_amount_validator(amount)

        coupon = Coupon(Brand(brand_id), discount)
        created = 0  # Want to make sure response code is valid if no codes were created

        for c in create_coupons(coupon, amount):
            STORAGE.add(c)
            created += 1

        return HttpResponse(status=201 if created else 204)


class CouponClaimView(APIView):

    def post(self, request):
        data = request.data
        brand_id = data.get('brand_id')
        _data = data.get('data', {})
        email = _data.get('email')
        discount = _data.get('discount')

        validators.coupon_discount_validator(discount)
        validators.email_validator(email)

        if already_claimed(User(email, coupon=True if email == settings.TEST_CLAIMED_EMAIL else None)):
            raise AlreadyClaimed(f"User {email} already claimed a coupon")

        if not brand_exists(Brand(brand_id)):
            raise NotFound(f"Brand {brand_id} does not exist")

        coupon = Coupon(brand=Brand(brand_id), discount=discount)
        claimed = claim_coupon(coupon, storage=STORAGE)

        if not claimed:
            raise NotFound(f"No coupons found for brand {brand_id} with discount {discount}")

        return JsonResponse(
            data={
                "discount_code": claimed.code,
                "discount": claimed.discount,
                "claimed": claimed.claimed_at
            })
