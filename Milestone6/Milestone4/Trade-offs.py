from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (i, j)
    return None
res = find_sum(5, [1, 2, 3, 4, 5])
print(res)
print("O(n*2)")
