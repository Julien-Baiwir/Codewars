"""Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28"""

def century(year):
    century = year // 100
    if year % 100 != 0:
        century += 1   
    return century  

def century(year):
    return (year + 99) // 100

import math

def century(year):
    return math.ceil(year / 100)

def century(year):
    if year%100==0:
        return year//100
    else:
        return year//100+1
