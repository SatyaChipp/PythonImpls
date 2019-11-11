# -*- coding: utf-8 -*-


"""
Given an integer, , print the following values for each integer  from  to :
Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be 
space-padded to match the width of the binary value of .
"""


def print_formatted(number):
    # your code goes here
    
    # width = len("{0:b}".format(number)) #binary value of n
    # for i in range(1, number+1):
    #     print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        print (str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')

if __name__ == '__main__':
    print_formatted(27)