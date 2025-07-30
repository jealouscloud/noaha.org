from typing import NamedTuple

from sqlalchemy import CursorResult


def param_check(result: CursorResult, named_tuple: type[NamedTuple]):
    """
    raise ValueError if result columns
    """
    keys = tuple(result.keys())
    if keys != named_tuple._fields:
        raise ValueError(f"Expected keys {keys}, but got {named_tuple._fields}")
