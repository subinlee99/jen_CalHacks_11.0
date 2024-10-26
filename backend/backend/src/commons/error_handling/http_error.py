"""
Implementation of the http error
"""

import logging
import traceback

from ..error_handling.base_error import BaseError

logger = logging.getLogger("HttpError")


class HttpError(BaseError):
    """
    Encapsulate logic for http error at the API layer

    handle any error specific to route validation errors (eg. Validation error)
    """

    status_code = 422

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message=message, status_code=status_code, payload=payload)
        self.log_error()

    def log_error(self):
        stack_trace = traceback.format_exc()
        logger.error(
            f"HTTP Error occurred: {self.message} | Status Code: {self.status_code} | Payload: {self.payload}\nStack Trace:\n{stack_trace}"
        )
