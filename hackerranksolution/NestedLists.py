"""
@author geekyharsh05

Nested Lists

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N, the number of students. The 2N subsequent lines describe each student over 2 lines.

- The first line contains a student's name.
- The second line contains their grade.


Constraints

2 <= N <= 5
There will always be one or more students having the second lowest grade. 

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

The Solution is given below
"""

if __name__ == '__main__':
    li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
scr = [x[1] for x in li]
min_li = sorted(set(scr))
stud = sorted([y[0] for y in li if y[1] == min_li[1]])
[print(k) for k in stud]