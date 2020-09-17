# Cyclic Rotation
from collections import deque
def solution(A, K):
    dlist = deque(A)
    dlist.rotate(K)
    return list(dlist)

# Odd Occurences In An Array
def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result
