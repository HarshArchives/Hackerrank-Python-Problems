"""
@author geekyharsh05

Swap Case

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

    string s: the string to modify

Returns

    string: the modified string

Input Format

A single line containing a string s.

Constraints

0 < len(s) <= 1000

The Solution is given below
"""


def swap_case(s):
    return s.swapcase()  # using swapcase function


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)