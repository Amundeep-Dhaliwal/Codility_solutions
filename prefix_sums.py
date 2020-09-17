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
