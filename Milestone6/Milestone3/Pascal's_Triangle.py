from typing import List

def get_triangle(rows: int) -> List[List[int]]:
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_triangle(triangle: List[List[int]]) -> None:
    rows = len(triangle)
    for i in range(rows):
        print(' ' * (rows - i), end='')
        print(' '.join(str(num) for num in triangle[i]))

triangle = get_triangle(5)
print_triangle(triangle)