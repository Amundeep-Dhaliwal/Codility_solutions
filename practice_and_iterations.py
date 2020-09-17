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
