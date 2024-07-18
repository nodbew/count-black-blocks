from core.input_support import recurse, catch_error
from core.calculation import read_from_input, construct_cuboid, count

@recurse
@catch_error
def main() -> None:
    # Recieve the input
    print("Enter the size of the cuboid...(type in help for documentation)")
    user_input = input()

    if user_input == 'q':
        exit()
    elif user_input == 'help':
        with open('./doc/doc.txt', 'r', encoding = 'utf-8') as f:
            print(f.read()[:-29]) # To truncate the comment: 'A nice ASCII art, isn't it?'
        print("Type in 'q' to quit.")
        return
    else:
        try:
            cuboid_size = tuple(map(int, user_input.split()))
            if len(cuboid_size) != 3:
                raise ValueError("Invalid cuboid size: please type in 3 numbers")
        except Exception as e:
            print("Invalid input. Error:", e)
            return
    
    # Count black blocks
    faces = read_from_input(cuboid_size)
    cuboid = construct_cuboid(*faces)
    print("The number of black blocks is:", count(cuboid))

    return
