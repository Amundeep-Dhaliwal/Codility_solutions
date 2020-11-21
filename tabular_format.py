# This is my revisited solution to a codility question that I was set

# Essentially prints an array of positive integers in a tabular format (A)
# You can specify the number of cells on a row (K)
# The width of every cell corresponds string length of the largest integer in the array

def solution(A, K): 
    width = len(str(max(A)))
    if K>len(A):
        newLineAfter = len(A)
        print(('+'+'-'*width)*newLineAfter+'+')
        for index in range(newLineAfter):
            numberWidth = len(str(A[index]))
            print('|'+' '*(width-numberWidth)+str(A[index]), end='')
        print('|')
        print(('+'+'-'*width)*newLineAfter + '+')
    else:
        rectangles = K
        print(('+'+ ('-'*width))*rectangles+'+')
        newLineList = [x-1 for x in range(0, len(A), K)]
        for index in range(len(A)):
            numberWidth = len(str(A[index]))
            print('|' + ' '*(width - numberWidth) + str(A[index]), end='')
            if index in newLineList:
                print('|')
                print(('+' + '-'*width)*rectangles+'+')
        print('|')
        lastRep = (len(A)%K) if len(A)%K != 0 else K
        print(('+' + '-'*width)*lastRep +'+')

        
