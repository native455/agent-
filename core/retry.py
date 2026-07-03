"""
Retry Engine

MyAgent V12

Provides automatic retry support for tool execution.
"""

import time


DEFAULT_RETRIES = 3
DEFAULT_DELAY = 0.5


def retry(func, *args,
          retries=DEFAULT_RETRIES,
          delay=DEFAULT_DELAY,
          **kwargs):
    """
    Execute a function with automatic retries.

    Returns:

    success (bool)
    result
    attempts
    """

    attempts = 0

    while attempts < retries:

        attempts += 1

        try:

            result = func(*args, **kwargs)

            return True, result, attempts

        except Exception as e:

            error = e

            if attempts < retries:
                time.sleep(delay)

    return False, str(error), attempts
