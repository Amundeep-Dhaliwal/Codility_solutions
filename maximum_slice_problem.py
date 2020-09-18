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
