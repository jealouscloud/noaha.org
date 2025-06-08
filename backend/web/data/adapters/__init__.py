from typing import NamedTuple


def type_check(named_tuple: NamedTuple):
    for argname, expected_type in named_tuple.__annotations__.items():
        actual_value = getattr(named_tuple, argname)
        if not isinstance(actual_value, expected_type):
            raise TypeError(
                f"Argument '{argname}' expected {expected_type.__name__ if hasattr(expected_type, '__name__') else expected_type}, "
                f"got {type(actual_value).__name__}"
            )
