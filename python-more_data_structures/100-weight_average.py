#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_weights = 0
    s = 0
    for t in my_list:
        s += t[0] * t[1]
        sum_weights += t[1]
    return s / sum_weights
