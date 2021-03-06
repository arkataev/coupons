from rest_framework.views import exception_handler


def coupons_exceptions_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response
