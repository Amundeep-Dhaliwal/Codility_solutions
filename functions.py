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

# Genomic Range Query
def solution(S, P, Q):
    result = list()
    for index in range(len(P)):
        if 'A' in S[P[index]:Q[index] + 1]:
            result.append(1)
        elif 'C' in S[P[index]:Q[index]+1]:
            result.append(2)
        elif 'G' in S[P[index]:Q[index]+1]:
            result.append(3)
        else:
            result.append(4)
    return result

# Minimum Average Two Slice
def solution(A):
    min_avg_value = (A[0] + A[1])/2.0
    min_avg_pos = 0
    for index in range(len(A) -2):
        if (A[index] + A[index+1]) /2 < min_avg_value:
            min_avg_value = (A[index]+A[index+1])/2
            min_avg_pos = index
        if (A[index]+A[index+1]+A[index+2])/3 < min_avg_value:
            min_avg_value =(A[index] + A[index+1] + A[index+2])/3
            min_avg_pos = index
    if (A[-1] + A[-2])/2 <min_avg_value:
        min_avg_value = (A[-1]+A[-2])/2
        min_avg_pos = len(A)-2
    return min_avg_pos

# Passing Cars
def solution(A):
    zero_count = 0
    combinations = 0
    for item in A:
        if item ==0:
            zero_count += 1
        else:
            combinations += zero_count
        
        if combinations > 1_000_000_000:
            return -1
    return combinations

# Distinct
def solution(A):
    return len(set(A))

# Max Product Of Three
def solution(A):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1]*A[-2]*A[-3])

# Number Of Disc Intersections
def solution(A): # number of disk intersections solution
    import bisect
    if len(A) <= 1:
        return 0 
    cuts = [(c-r, c+r) for c, r in enumerate(A)]
    cuts.sort(key=lambda pair: pair[0]) # sort the tuples based on their first element
    #print(cuts)
    lefts, rights = zip(*cuts)
    total = 0
    bRight = bisect.bisect_right
    for i in range(len(A)):
        r = rights[i] 
        pos = bRight(lefts, r)
        total += (pos - i - 1)
        if total > 10e6:
            return -1
    return total
