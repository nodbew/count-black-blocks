from functools import wraps
from .errors import TypeAssertionError, InhomogeneousShapeError

def recurse(func: Callable) -> Callable:
    '''
    Repeat the function forever.
    '''
    @wraps(func)
    def _wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
    return _wrapper


def catch_error(func: Callable) -> Callable:
    '''
    Catches the error and display it. 
    Finally, clears the console.
    '''
    @wraps(func)
    def _wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeAssertionError as e:
            print("Invalid type detected. Error:", e)
            return
        except InhomogenousShapeError as e:
            print("The face was not a rectangle. Please type in a valid cuboid. Error:", e)
            return
        except Exception as e:
            print("Error:", e)
            return
    return _wrapper
