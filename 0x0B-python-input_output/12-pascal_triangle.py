#!/usr/bin/python3
# 12-pascal_triangle.py
""" Python """


def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        x_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(x_row[j - 1] + x_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
