from app.libs.error import APIException


class ClientSuccess(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(ClientSuccess):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake!'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource is not found!'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed!'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    msg = 'forbidden'
    error_code = 1004


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
