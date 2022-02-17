from rest_framework.exceptions import APIException


class AlreadyClaimed(APIException):
    status_code = 409
