"""
@author geekyharsh05

Loops

Task

The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n , print i^2. 

Input Format

The first and only line contains the integer, n.

Constraints

1 <= n <= 20

Output Format

Print n lines, one corresponding to each i. 

The Solution is given below
"""

n = int(input()) # Taking user input
for i in range(0,n):  # using for loop printing n times
    print(i ** 2);    # printing the square of each number