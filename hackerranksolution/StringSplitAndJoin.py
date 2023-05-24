"""
@author geekyharsh05

In Python, a string can be split on a delimiter.

Example:
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

Joining a string is simple:
>>> a = "-".join(a)
>>> print a
this-is-a-string 

Task 
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format 
The first line contains a string consisting of space separated words.

Output Format 
Print the formatted string as explained above.

Sample Input
this is a string   

Sample Output
this-is-a-string


The Solution is given below
"""


def split_and_join(line):
    # Split the line into a list of words using whitespace as the separator
    words = line.split()

    # Join the words in the list using a hyphen as the separator
    joined_line = "-".join(words)

    # Return the joined line
    return joined_line


if __name__ == '__main__':
    # Get user input for the line
    line = input()

    # Call the split_and_join function to process the line
    result = split_and_join(line)

    # Print the result
    print(result)
