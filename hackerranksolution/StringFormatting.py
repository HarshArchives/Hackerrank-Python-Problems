"""
@author geekyharsh05

The Solution is given below
"""


def print_formatted(number):
    w = n.bit_length()
    for num in range(1, n + 1):
        print(f"{num:>{w}d} {num:>{w}o} {num:>{w}X} {num:>{w}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
