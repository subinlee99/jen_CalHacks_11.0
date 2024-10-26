"""
Implementation of the repository error
"""

from ..error_handling.base_error import BaseError

import logging
import traceback

logger = logging.getLogger("RepositoryError")


class RepositoryError(BaseError):
    """
    Encapsulate logic for Repository error at the data layer
    handle any errors related to the data retrieval

    Examples:

    Connection (cannot establish connection with DB)

    DuplicateKey (record with same id exists)

    RecordNotFound
    """

    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message=message, status_code=status_code, payload=payload)
        self.log_error()

    def log_error(self):
        stack_trace = traceback.format_exc()
        logger.error(
            f"Repository Error occurred: {self.message} | Status Code: {self.status_code} | Payload: {self.payload}\nStack Trace:\n{stack_trace}"
        )
