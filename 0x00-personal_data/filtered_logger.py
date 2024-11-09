#!/usr/bin/env python3
"""
Module for filtering log messages to obfuscate PII fields.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of fields to obfuscate.
        redaction: The string to replace the field values.
        message: The log message to process.
        separator: The separator character in the log message.

    Returns:
        The obfuscated log message as a string.
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+", f"{field}={redaction}", message)
    return message
