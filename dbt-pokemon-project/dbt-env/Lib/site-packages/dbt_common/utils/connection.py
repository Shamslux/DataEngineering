import time
from typing import Callable

from dbt_common.events.types import RecordRetryException, RetryExternalCall
from dbt_common.exceptions import ConnectionError
from tarfile import ReadError

import requests


def connection_exception_retry(fn: Callable, max_attempts: int, attempt: int = 0):
    """Handle connection retries gracefully.

    Attempts to run a function that makes an external call, if the call fails
    on a Requests exception or decompression issue (ReadError), it will be tried
    up to 5 more times.  All exceptions that Requests explicitly raises inherit from
    requests.exceptions.RequestException.  See https://github.com/dbt-labs/dbt-core/issues/4579
    for context on this decompression issues specifically.
    """
    try:
        return fn()
    except (
        requests.exceptions.RequestException,
        ReadError,
        EOFError,
    ) as exc:
        if attempt <= max_attempts - 1:
            # This import needs to be inline to avoid circular dependency
            from dbt_common.events.functions import fire_event

            fire_event(RecordRetryException(exc=str(exc)))
            fire_event(RetryExternalCall(attempt=attempt, max=max_attempts))
            time.sleep(1)
            return connection_exception_retry(fn, max_attempts, attempt + 1)
        else:
            raise ConnectionError("External connection exception occurred: " + str(exc))
