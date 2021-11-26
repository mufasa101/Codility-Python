# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    chop_1=A[0]
    chop_2=sum(A[1:])
    min_diff=abs(chop_1-chop_2)
    for i in range(1,len (A)-1):
        chop_1+=A[i]
        chop_2-=A[i]
        if abs(chop_1-chop_2) < min_diff:
            min_diff=abs(chop_1-chop_2)
    return min_diff
        
        

def solution(A):
    chop_1=A[0]
    chop_2=sum(A[1:])
    min_diff=abs(chop_1-chop_2)
    for i in range(1,len (A)-1):
        chop_1+=A[i]
        chop_2-=A[i]
        if abs(chop_1-chop_2) < min_diff:
            min_diff=abs(chop_1-chop_2)
    return min_diff
        
        



import sys

def solution(A):
    # write your code in Python 3.6
    
    INT_MAX = sys.maxsize
    INT_MIN = -sys.maxsize-1
    
    min_diff = INT_MAX
    
    for index in range(0, len(A) ):
        
        first_total = 0
        for j in range(0, index):
            first_total += A[j]
        
        second_total = 0
        for k in range(index, len(A) ):
            second_total += A[k]
        
        current_difference = abs( first_total - second_total )
        
        min_diff = min( min_diff, current_difference )
    
    return min_diff
