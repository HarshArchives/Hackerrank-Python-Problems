"""
@author geekyharsh05

The given code is a Python function is_leap() that checks whether a given year is a leap year or not. The approach used in the code is based on the rules for leap years:

    1. A year is a leap year if it is divisible by 4.
    2. However, if a year is divisible by 100, it is not a leap year, unless:
    3. The year is also divisible by 400, in which case it is a leap year.

    Here's a breakdown of the approach used in the code:

    1. The function is_leap(year) takes an input parameter year to check if it is a leap year.
    2. It initializes a boolean variable leap as False to represent that the year is not a leap year by default.
    3. The code then uses nested if statements to check the conditions for a leap year.
    4. The first if statement (year % 4) == 0 checks if the year is divisible by 4.
    5. If it is divisible by 4, the code proceeds to the inner if statement (year % 100) == 0 to check if the year is divisible by 100.
    6. If the year is divisible by 100, it enters the innermost if statement (year % 400) == 0 to check if it is also divisible by 400.
    7. If the year is divisible by 400, the variable leap is set to True since it satisfies all the conditions for a leap year.
    8. If the year is divisible by 4 but not by 100 or by 400, the variable leap is also set to True because it satisfies the conditions for a leap year.
    9. If the year is not divisible by 4 or it is divisible by 100 but not by 400, the variable leap remains False.
   10. Finally, the function returns the value of leap.
   11. The code prompts the user to input a year and passes it to the is_leap() function. The result is then printed to the console.

   Overall, the code implements the logic of checking for leap years according to the specified rules and returns the result.

The Solution is given below
"""

def is_leap(year):
    """
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - leap (bool): True if the year is a leap year, False otherwise.
    """

    # variable to check the leap year
    leap = False

    # using nested if statements
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

# Prompt the user to input a year
year = int(input("Enter a year: "))

# Call the is_leap() function with the input year and print the result
print(is_leap(year))
