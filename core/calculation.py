import numpy as np

from .errors import TypeAssertionError, InhomogeneousShapeError
from .typecheck import check_type

@check_type
def read_from_input(cuboid_size: tuple) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    '''
    Takes the size of the cuboid, and reads the input from the user.
    The input will be formatted into 3 2-dimensional ndarrays, each representing a face of the cuboid.
    '''
    # Read input from the user
    cuboid = np.zeros(cuboid_size)
    a, b, c = [], [], []
    print("Please enter the faces of the cuboid(0 is white, 1 is black. Split by white spaces)")
    for _ in range(cuboid_size[2]):
        a.append(list(map(int, input().split())))
    for _ in range(cuboid_size[1]):
        b.append(list(map(int, input().split())))
    for _ in range(cuboid_size[0]):
        c.append(list(map(int, input().split())))

    # Convert to numpy arrays
    try:
        a = np.array(a, dtype = np.int8)
        b = np.array(b, dtype = np.int8)
        c = np.array(c, dtype = np.int8)
    except ValueError as e:
        if "inhomogeneous" in str(e):
            raise InhomogeneousShapeError("Inhomogenous shape")
        elif "invalid literal for int()" in str(e):
            raise TypeAssertionError(str(e))
        else:
            raise ValueError(e)

    return a, b, c

@check_type
def construct_cuboid(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    '''
    Takes the three faces of the cuboid and return the cuboid as a 3-dimensional ndarray.
    '''

    # Get the size of the cuboid
    w = a.shape[1]
    h = b.shape[0]
    l = c.shape[1]
    # Construct cuboid based on the size
    cuboid = np.zeros((l, h, w))

    # Fill black blocks
    cuboid[c == 1] = 1
    cuboid[:, a == 1] = 1
    cuboid = np.rot90(cuboid, axes = (1, 2))
    cuboid[np.fliplr(b) == 1] = 1

    return np.rot90(cuboid, axes = (2, 1))

@check_type
def count(cuboid: np.ndarray) -> int:
    '''
    Counts the number of black blocks in the cuboid.
    '''
    return int(np.sum(cuboid))
