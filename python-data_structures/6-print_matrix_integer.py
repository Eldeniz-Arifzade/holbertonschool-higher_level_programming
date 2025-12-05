#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for entry_idx in range(len(row)):
            if entry_idx == len(row) - 1:
                print('{:d}'.format(row[entry_idx]))
            else:
                print('{:d}'.format(row[entry_idx]), end=' ')
        print()
