#!/usr/bin/python3
"""This module will define a function which will return Pascal's Triangle"""


def pascal_triangle(n):
    """This function will return n-th order Pascal traingles in list of lists"""
    if n<= 0:
        return []
    l[0][0] = 0
    for i in range(1, n-1):
        l[i][0] = 1
        l[i][i] = 1
        for j in range(1, i):
            l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l
