#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            # Check if the current number is not the last number in the row
            if num in row[:-1]:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print("")
