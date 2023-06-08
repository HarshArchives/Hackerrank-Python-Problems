"""
@author geekyharsh05
    The first line reads an input string from the user.
    The second line checks if there is any alphanumeric character in the string and prints the result.
    The third line checks if there is any alphabetic character in the string and prints the result.
    The fourth line checks if there is any digit in the string and prints the result.
    The fifth line checks if there is any lowercase letter in the string and prints the result.
    The sixth line checks if there is any uppercase letter in the string and prints the result.

The Solution is given below
"""
if __name__ == '__main__':
    s = input()
    print(any(a.isalnum() for a in s))
    print(any(a.isalpha() for a in s))
    print(any(a.isdigit() for a in s))
    print(any(a.islower() for a in s))
    print(any(a.isupper() for a in s))
