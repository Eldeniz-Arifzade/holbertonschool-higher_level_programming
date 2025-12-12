#!/usr/bin/python3
"""This module will define a function which will return Pascal's Triangle"""


def pascal_triangle(n):
    """Function will return n-th order Pascal traingles in list of lists"""
    if n <= 0:
        return []
    list_pascal = [[1]*i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            list_pascal[i][j] = list_pascal[i-1][j-1] + list_pascal[i-1][j]
    return list_pascal
