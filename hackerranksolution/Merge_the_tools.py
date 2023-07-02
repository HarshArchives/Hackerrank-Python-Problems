""""
@author geekyharsh05

The function merge_the_tools divides the string into equal parts of length k and removes duplicate characters before printing.

The Solution is given below
"""


def merge_the_tools(string, k):
    # your code goes here
    l = len(string)//k
    for i in range(l):
        print(''.join(dict.fromkeys(string[i*k:(i*k)+k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)