"""
@author geekyharsh05

    Read the input: Start by reading the input for the thickness of the logo. The thickness determines the size of the logo and the number of characters used in each line.

    Print the top cone: Use a loop to iterate from 0 to thickness-1. In each iteration, print a line that consists of the character repeated i times, right justified with (thickness-1-i) spaces, followed by the character repeated i times, left justified with (thickness-1-i) spaces.

    Print the top pillars: Use another loop to iterate from 0 to thickness. In each iteration, print a line that consists of the character repeated thickness times, centered in a string of length (thickness * 2), followed by the same pattern repeated twice, centered in a string of length (thickness * 6).

    Print the middle belt: Use another loop to iterate (thickness+1)//2 times. In each iteration, print a line that consists of the character repeated (thickness * 5), centered in a string of length (thickness * 6).

    Print the bottom pillars: Repeat the same logic as step 3, printing the same pattern as the top pillars.

    Print the bottom cone: Use a loop to iterate from 0 to thickness-1. In each iteration, print a line that consists of the character repeated (thickness - i - 1) times, right justified with thickness spaces, followed by the character, followed by the character repeated (thickness - i - 1) times, left justified with thickness spaces. Right justify the entire line with (thickness * 6) spaces.

The Solution is given below
"""
# Text Alignment Hackerrank Solution

thickness = int(input())  # Read input for thickness of the logo
c = 'H'  # Character used for the logo

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c +
           (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
