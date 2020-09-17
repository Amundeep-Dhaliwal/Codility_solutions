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
