"""
@author geekyharsh05

    The function takes two parameters: string and sub_string.
    It uses a list comprehension and the startswith method to iterate over each index i in the range of the length of the string.
    For each index, it checks if the substring starting from that index matches the given substring.
    It sums up the number of matches found and returns the count.

The Solution is given below
"""
def count_substring(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
