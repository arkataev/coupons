from flask import jsonify
from flask import request
from flask.views import MethodView

from src.coupons.claiming import claim_coupon
from src.coupons.common import Brand, Coupon
from src.coupons.storage import CouponHeapStorage
from src.coupons.generate import create_coupons


class CouponClaimView(MethodView):
    methods = ['POST']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._brands = set()
        self._claimed = set()
        self._coupons_storage = CouponHeapStorage()
        self.init_data()

    def init_data(self):
        self._brands.add('12345')
        self._claimed.add('claimed@email.com')

        for c in create_coupons(Coupon(brand=Brand('12345'), discount=0.2), 10):
            self._coupons_storage.add(c)

    def post(self):
        # TODO:: Authorize User
        data = request.json
        brand_id = data.get('brand_id')
        email = data.get('data', {}).get('email')

        if email in self._claimed:
            return jsonify(
                {"error": "validation_error",
                 "field": "email",
                 "message": f"email {email} already claimed coupon"}
            ), 409

        if brand_id not in self._brands:
            return jsonify(
                {"error": "not_found",
                 "field": "brand_id",
                 "message": f"brand {brand_id} does not exist"}
            ), 404

        coupon = claim_coupon(brand=Brand(brand_id), storage=self._coupons_storage)

        if not coupon:
            return jsonify(
                {"error": "not_found",
                 "field": "",
                 "message": f"no coupons found for brand {brand_id}"}
            ), 404

        self._claimed.add(email)

        return jsonify({"discount_code": coupon.code, "discount": coupon.discount, "claimed": coupon.claimed_at}), 200
