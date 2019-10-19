"""Custom exceptions"""

import quart.exceptions as qexc
from http import HTTPStatus


class QuartSmorestError(Exception):
    """Generic flask-smorest exception"""


class OpenAPIVersionNotSpecified(QuartSmorestError):
    """OpenAPI version was not specified"""


class CheckEtagNotCalledError(QuartSmorestError):
    """ETag enabled on resource but check_etag not called"""


class NotModified(qexc.HTTPStatusException, QuartSmorestError):
    """Resource was not modified (Etag is unchanged)

    Exception created to compensate for a lack in Werkzeug (and Flask)
    """
    status = HTTPStatus.NOT_MODIFIED


class PreconditionRequired(qexc.HTTPException, QuartSmorestError):
    """Etag required but missing"""
    # Overriding description as we don't provide If-Unmodified-Since
    status = HTTPStatus.PRECONDITION_REQUIRED


class PreconditionFailed(qexc.HTTPStatusException, QuartSmorestError):
    """Etag required and wrong ETag provided"""
    status = HTTPStatus.PRECONDITION_FAILED
