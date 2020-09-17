# Dominator
from collections import Counter
def solution(A):
    length = len(A)
    if length < 1:
        return -1
    countDict = Counter(A)
    mostCommon = countDict.most_common()[0]
    if mostCommon[1] > int(length/2):
        return A.index(mostCommon[0])
    else:
        return -1
    
# Equilibrium Leader
from collections import defaultdict
def solution(A):
    markerLeft = defaultdict(lambda : 0)
    markerRight = defaultdict(lambda : 0)
    for i in range(len(A)):
        markerRight[A[i]]+=1
    numberLeaders= 0
    leader =A[0]
    for i in range(len(A)):
        markerRight[A[i]]-=1
        markerLeft[A[i]]+=1
        if i== 0 or markerLeft[leader]<markerLeft[A[i]]:
            leader= A[i]
        
        if (i+1)//2 <markerLeft[leader] and (len(A) -(i+1))//2<markerRight[leader]:
            numberLeaders+= 1
    return numberLeaders
