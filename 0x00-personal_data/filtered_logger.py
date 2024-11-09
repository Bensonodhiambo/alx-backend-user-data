#!/usr/bin/env python3
"""
Module for logging user data with sensitive information obfuscation.
"""

import logging
import re
from typing import List, Tuple

# Define sensitive fields to be redacted
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+", f"{field}={redaction}",
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for logging sensitive information."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to be redacted."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record to redact sensitive information.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data'.

    Returns:
        logging.Logger: Configured logger instance with sensitive data
                        obfuscation.
    """
    # Create a logger with the specified name
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Prevent log propagation

    # Create a StreamHandler with RedactingFormatter using PII_FIELDS
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        RedactingFormatter(fields=PII_FIELDS)
    )

    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger
