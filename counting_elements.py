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
