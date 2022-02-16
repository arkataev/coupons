from flask import Flask
from . import views

app = Flask(__name__)

# Register endpoints
app.add_url_rule('/api/v1/codes/claim', view_func=views.CouponClaimView.as_view('claim_coupon'))
