from functools import wraps
from typing import Callable
from inspect import signature
from errors import TypeAssertionError

def check_type(func: Callable) -> Callable:
    '''
    Ensures that the type of arguments matches the type annotation.
    '''
  
    @wraps(func)
    def _wrapper(*args, **kwargs):
        sig = signature(func)

        for param, (_, arg) in zip(sig.parameters.values(), enumerate(args)):
            if param.annotation == param.__class__.empty:
                continue
            else:
                if not isinstance(arg, param.annotation):
                    raise TypeAssertionError(f"Invalid type for argument {param.name}: expected {param.annotation} instance, found {arg.__class__}")

        for kw, arg in kwargs.items():
            if kw in sig.parameters:
                if not isinstance(arg, sig.parameters[kw].annotation):
                    raise TypeAssertionError(f"Invalid type for argument {kw}: expected {sig.parameters[kw].annotation} instance, found {arg.__class__}")
            else:
                raise ValueError(f"Invalid keyword argument {kw}")

        return func(*args, **kwargs)

    return _wrapper
