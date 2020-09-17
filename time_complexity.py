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
