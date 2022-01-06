#!/usr/bin/env python3
"""Personal data"""
from typing import List
import re
import logging


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    '''returns the log message obfuscated'''
    for pii in fields:
        message = re.sub(fr'{pii}=.+?{separator}',
                         f'{pii}={redaction}{separator}', message)
    return message
