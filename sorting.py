# Distinct
def solution(A):
    return len(set(A))

# Max Product Of Three
def solution(A):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1]*A[-2]*A[-3])

# Number Of Disc Intersections
from bisect import bisect_right, bisect_left
def solution(A):
    start = [center - radius for center, radius in enumerate(A)]
    start.sort()
    pairs = 0
    for i in range(len(A)):
        end = i + A[i]
        count = bisect_right(start,end)-1
        count_1 = count - i
        pairs += count_1
        if pairs > 10_000_000:
            return -1
    return pairs

# Triangle
def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
