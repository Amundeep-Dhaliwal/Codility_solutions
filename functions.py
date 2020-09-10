# Missing Integer
def solution(A):
    missing = 1
    setA = set(A)
    while missing in setA:
        missing += 1
    return missing

# Binary Gap 
import re
def solution(N):
    stringRep = format(N, 'b')
    lengths = (re.findall(r'1(0+)(?=1)', stringRep))
    rv = len(max(lengths, key = len)) if lengths else 0
    return rv

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

# Frog Jump
def solution(start,stop, step):
    if (stop - start) % step == 0:
        return (stop - start)//step
    else:
        return (stop - start) // step + 1

# Permutation Missing Element
def solution(A):
    A = set(A)
    missing = 1
    while missing in A:
        missing += 1
    return missing

# Tape Equilibrium
def solution(A):
    summation = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(left_sum*2 - summation), m)
    return m

