"""
@author geekyharsh05

This code defines a function called solve that takes a string s as input and capitalizes the first letter of each word in the string. It then returns the modified string with the capitalized words joined by spaces.

    The function uses a list comprehension to split the input string s into individual words using the space character as the delimiter. It then iterates over each word and applies the capitalize() method to capitalize the first letter of each word.
    The capitalized words are collected back into a list using the list comprehension.
    The join() method is used to concatenate the capitalized words into a single string, with each word separated by a space.
    In the if __name__ == '__main__': block, the code opens a file specified by the OUTPUT_PATH environment variable in write mode. It reads a string s from the user and calls the solve function with s as the argument. The resulting modified string is written to the file, followed by a newline character, and the file is closed.

The Solution is given below
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join([name.capitalize() for name in s.split(" ")])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
