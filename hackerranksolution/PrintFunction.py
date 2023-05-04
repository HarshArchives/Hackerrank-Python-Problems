"""
@author geekyharsh05

Print Function

The included code stub will read an integer,n , from STDIN.

Without using any string methods, try to print the following:
1,2,3...n

Note that "..." represents the consecutive values in between.

Input Format

The first line contains an integer n.

Constraints

1 <= n <= 150

Output Format

Print the list of integers from 1 through n as a string, without spaces.

The Solution is given below
"""

n = int(input()) 
print(*[i for i in range(1,n+1)],sep="") # using list comprehension