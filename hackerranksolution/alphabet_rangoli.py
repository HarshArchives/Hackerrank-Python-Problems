"""
@author geekyharsh05

This code defines a function called print_rangoli that takes an integer parameter size as input. It generates a pattern resembling a rangoli, which is a traditional Indian decorative art form.

    It constructs the pattern by creating a string of alphabets in descending order and separating them with hyphens.
    It then iterates over a range of values from 1 to size * 2 (inclusive) with a step size of 2. For each value, it constructs a layer of the rangoli pattern by slicing and concatenating the alphabets string.
    The constructed layer is centered within a string of hyphens with a length of size * 4 - 3 and added to a list called layers.
    Finally, it prints the layers in reverse order, excluding the last layer, to form the complete rangoli pattern.

In the if __name__ == '__main__': block, the code reads an integer n from the user and calls the print_rangoli function with n as the argument to generate and print the rangoli pattern.

The Solution is given below
"""


def print_rangoli(size: int):
    pattern = '-'.join(chr(ch) for ch in reversed(range(ord('a'), ord('a') + size)))
    layers = []
    for limit in range(1, size * 2, 2):
        layer = f'{pattern[:limit]}{pattern[:limit - 1][::-1]}'
        layers.append(f'{layer:-^{size * 4 - 3}}')
        print(layers[-1])
    print('\n'.join(reversed(layers[:-1])))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)