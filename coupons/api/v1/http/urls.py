from django.urls import path

from . import views

urlpatterns = [
    path('coupons/claim', views.CouponClaimView.as_view(), name='coupons-claim'),
    path('coupons', views.CouponView.as_view(), name='coupons'),
]
