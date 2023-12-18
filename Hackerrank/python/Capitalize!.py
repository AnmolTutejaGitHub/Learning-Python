#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    l = s.split(' ')
    output = ''
    for index, i in enumerate(l):
        if i[0] == '0' or i[0] == '1' or i[0] == '2' or i[0] == '3' or i[0] == '4' or i[0] == '5' or i[0] == '6' or i[0] == '7' or i[0] == '8' or i[0] == '9':
            output += i+' '
        elif l[index] == len(l)-1:
            output += i[0].upper()+i[1:]

        else:
            output += i[0].upper()+i[1:]+' '
    return output


if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)
