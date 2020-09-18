# Max Double Slice Sum
def solution(A):
    mid = 1
    total = 0
    max_slice=0
    for index ,end in enumerate(A[2:-1],start=2):
        if total < 0:
            mid =index
            total = 0
        elif total == 0 and A[index-1]>A[mid]:
            mid =index -1
            total = end
        else:
            if A[mid] > end:
                total+=A[mid]
                mid = index
            else:
                total += end
        max_slice = max(max_slice,total)
    return max_slice

# Max Profit
def solution(A):
    minCost=200_000
    maxProfit = 0
    for cost in A:
        minCost = min(minCost,cost)
        maxProfit = max(maxProfit,cost-minCost)
    return maxProfit

# Max Slice Sum
def solution(A):
    max_ending = max_slice = A[0]
    for i in range(1,len(A)):
        max_ending = max(max_ending+A[i],A[i])
        max_slice = max(max_slice,max_ending)
    return max_slice
