# Brackets
def solution(S):
    stack = []
    opening = {'{','[','('}
    validCombinations = {'()', '[]', '{}'}
    for bracket in S:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 0
            left = stack.pop()
            if left+bracket not in validCombinations:
                return 0
    if len(stack) != 0:
        return 0
    return 1

# Fish
def solution(A,B):
    survivals = 0
    stack = []
    for index in range(len(A)):
        if B[index] == 0:
            while len(stack) != 0:
                if stack[-1] > A[index]:
                    break
                else:
                    stack.pop()
            else:
                survivals += 1
        else:
            stack.append(A[index])
    survivals += len(stack)
    return survivals

# Nesting
def solution(S):
    validCombinations = {'{}','[]','()'}
    opening = {'(', '{','['}
    stack = []
    for bracket in S:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 0
            left = stack.pop()
            if (left + bracket) not in validCombinations:
                return 0
    if len(stack) != 0:
        return 0
    else:
        return 1

# Stone Wall
def solution(H):
    block_cnt = 0
    stack = []
    for height in H:
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
        if len(stack) != 0 and stack[-1] == height:
            pass
        else:
            block_cnt +=1 
            stack.append(height)
    return block_cnt
