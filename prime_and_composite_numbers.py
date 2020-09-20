# Count Factors
def solution(N):
    count = 0
    i = 1
    while (i **2 <= N):
        if N % i == 0:
            if i **2 == N:
                count += 1
            else:
                count += 2
        i += 1 
    return count
