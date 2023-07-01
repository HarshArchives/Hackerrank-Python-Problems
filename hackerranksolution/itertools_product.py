""""
@author geekyharsh05

The code takes two sets of input values, converts them to integers, computes all possible combinations of elements from the two sets, and prints the resulting combinations as output.

The Solution is given below
"""

from itertools import product

# Take input for list 'a' and convert each element to integer
a = map(int, input().split())

# Take input for list 'b' and convert each element to integer
b = map(int, input().split())

# Print the Cartesian product of lists 'a' and 'b'
print(*product(a, b))
