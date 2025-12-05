#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for entry_idx in range(len(row)):
            if entry == len(row) - 1:
                print('{:d}'.format(entry))
            else:
                print('{:d}'.format(entry), end=' ')
        print()
