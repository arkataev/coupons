from unittest import mock

import pytest
from django.urls import reverse


@pytest.fixture
def disable_validation():
    patches = [
        mock.patch('coupons.api.http.validators.email_validator'),
        mock.patch('coupons.api.http.validators.coupon_amount_validator'),
        mock.patch('coupons.api.http.validators.coupon_discount_validator'),
    ]
    for patch in patches:
        patch.start()
    yield
    for patch in patches:
        patch.stop()


def test_coupon_claim(client, coupon, disable_validation):
    with mock.patch('coupons.api.http.views.already_claimed', return_value=False):
        with mock.patch('coupons.api.http.views.brand_exists', return_value=True):
            with mock.patch('coupons.api.http.views.claim_coupon', return_value=coupon):
                response = client.post(reverse('coupons-claim'), data={}, format='json')

            assert response.status_code == 200


def test_coupon_already_claimed(client, coupon, disable_validation):
    with mock.patch('coupons.api.http.views.already_claimed', return_value=True):
        with mock.patch('coupons.api.http.views.brand_exists', return_value=True):
            with mock.patch('coupons.api.http.views.claim_coupon', return_value=coupon):
                response = client.post(reverse('coupons-claim'), data={}, format='json')

            assert response.status_code == 409


def test_coupon_brand_does_not_exist(client, coupon, disable_validation):
    with mock.patch('coupons.api.http.views.already_claimed', return_value=False):
        with mock.patch('coupons.api.http.views.brand_exists', return_value=False):
            with mock.patch('coupons.api.http.views.claim_coupon', return_value=coupon):
                response = client.post(reverse('coupons-claim'), data={}, format='json')

            assert response.status_code == 404


def test_coupon_no_coupons_found(client, disable_validation):
    with mock.patch('coupons.api.http.views.already_claimed', return_value=False):
        with mock.patch('coupons.api.http.views.brand_exists', return_value=True):
            with mock.patch('coupons.api.http.views.claim_coupon', return_value=None):
                response = client.post(reverse('coupons-claim'), data={}, format='json')

            assert response.status_code == 404


def test_generate_coupons(client, disable_validation, coupon):
    with mock.patch('coupons.api.http.views.brand_exists', return_value=True):
        with mock.patch('coupons.api.http.views.create_coupons', return_value=[coupon]):
            response = client.post(reverse('coupons'), data={}, format='json')

        assert response.status_code == 201


def test_generate_no_coupons(client, disable_validation, coupon):
    with mock.patch('coupons.api.http.views.brand_exists', return_value=True):
        with mock.patch('coupons.api.http.views.create_coupons', return_value=[]):
            response = client.post(reverse('coupons'), data={}, format='json')

        assert response.status_code == 204


def test_generate_no_brand(client, disable_validation, coupon):
    with mock.patch('coupons.api.http.views.brand_exists', return_value=False):
        with mock.patch('coupons.api.http.views.create_coupons', return_value=[]):
            response = client.post(reverse('coupons'), data={}, format='json')

        assert response.status_code == 404
