"""
@author geekyharsh05

Lists

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list. 

Input Format

The first line contains an integer i,, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

The Solution is given below
"""

# Pandey Ji Ka Method
if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        func, *args = input().split()
        if func != 'print':
            getattr(list, func)(*map(int, args))
        else:
            print(list)
