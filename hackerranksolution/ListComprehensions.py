"""
@author geekyharsh05

List Comprehensions

Input Format

Four integers x,y,z and n, each on a separate line. 

Constraints

Print the list in lexicographic increasing order.

The Solution is given below
"""

x, y, z, n = int(input()), int(input()), int(input()), int(input())
list = [[i, j, k]             # Using list comprehension
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i+j+k != n]
print(list)



