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

# Frog River One
def solution(X, A):
    leaves = {int(x+1) for x in range(X)}
    for index, value in enumerate(A):
        if value in leaves:
            leaves.discard(value)
            if leaves == set():
                return index
    return -1

# Max Counters
def solution(N,A): 
    config = [0] * N   
    maxVal = 0         
    currentMax = 0     
    for command in A:
        if 1 <= command <= N: 
            if config[command-1] < maxVal:
                config[command-1] = maxVal

            config[command-1] += 1 

            if config[command-1]>currentMax:
                currentMax= config[command-1]
        else:
            maxVal= currentMax
    for i in range(N):
        if config[i] < maxVal:
            config[i] = maxVal
    return config

# Missing Integer
def solution(A):
    A = set(sorted(A))
    num = 1
    while num in A:
        num += 1
    return num

# Permutation Check
def solution(A): 
    counter = [0] * len(A)
    limit = len(A)
    for element in A:
        if not 1 <= element <= limit:
            return 0
        else: 
            if counter[element - 1] != 0:
                return 0
            else:
                counter[element -1] = element
    return 1

# Count Divisions
def solution(A,B,K): 
    if A % K == 0: 
        return ((B- A) // K) +1 
    else: 
        return (B-(A- A %K)) // K
